import numpy as np
import pandas as pd
from src.var import Var
from src.var_type import VarType


class DatasetsGenerator:

    def get_noise_dataset(
            self,
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
        dep_df = self._get_noise_data()
        indep_df = self._get_noise()
        dep_df.columns = [f"Y_{k}" for k in range(1, dep_df.shape[1], 1)]
        dep_df.columns = [f"X_{k}" for k in range(1, indep_df.shape[1], 1)]
        return pd.concat([indep_vars, dep_vars], axis=0)

    @staticmethod
    def _get_noise_data(vars: list[Var], rows_num: int) -> pd.DataFrame:
        pass

    @staticmethod
    def _get_noise(var: Var, rows_num: int) -> np.array:
        if var.var_type == VarType.CONTINUOUS:
            return np.random.randn(rows_num)
        else:
            return np.random.randint(1, var.num_of_levels, size=rows_num)
