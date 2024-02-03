import numpy as np
import pandas as pd
from src.var import Var
from src.var_type import VarType


class DatasetsGenerator:

    @classmethod
    def get_generic_regression_dataset(cls, only_continuous_indep: bool = True):
        dep_vars = [Var(var_type=VarType.CONTINUOUS)] * 2
        indep_vars = [Var(var_type=VarType.CONTINUOUS)] * 5
        if not only_continuous_indep:
            indep_vars += [Var(var_type=VarType.BINARY)]
        return DatasetsGenerator.get_noise_dataset(dep_vars=dep_vars, indep_vars=indep_vars, rows_num=2_000, seed=321)

    @classmethod
    def get_generic_classification_dataset(cls, only_continuous_dep: bool = True):
        pass

    @classmethod
    def get_noise_dataset(
            cls,
            dep_vars: Var | list[Var],
            indep_vars: Var | list[Var],
            rows_num: int = 1_000,
            seed: int = 12345
    ) -> pd.DataFrame:
        if isinstance(dep_vars, Var):
            dep_vars = [dep_vars]
        if isinstance(indep_vars, Var):
            indep_vars = [indep_vars]
        np.random.seed(seed)
        dep_df = cls._get_noise_data(variabs=dep_vars, rows_num=rows_num)
        indep_df = cls._get_noise_data(variabs=indep_vars, rows_num=rows_num)
        dep_df.columns = [f"Y_{k}" for k in range(1, dep_df.shape[1] + 1, 1)]
        indep_df.columns = [f"X_{k}" for k in range(1, indep_df.shape[1] + 1, 1)]
        return pd.concat([dep_df, indep_df], axis=1)

    @classmethod
    def _get_noise_data(cls, variabs: list[Var], rows_num: int) -> pd.DataFrame:
        return pd.DataFrame(
            data=np.concatenate([cls._get_noise(var=var, rows_num=rows_num).reshape(-1, 1) for var in variabs], axis=1))

    @staticmethod
    def _get_noise(var: Var, rows_num: int) -> np.array:
        if var.var_type == VarType.CONTINUOUS:
            return np.random.randn(rows_num)
        else:
            return np.random.randint(1, var.num_of_levels, size=rows_num)
