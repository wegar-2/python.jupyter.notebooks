import numpy as np
import pandas as pd
from src.var import Var
from src.var_type import VarType
from sklearn.datasets import make_regression


class DatasetsGenerator:

    @classmethod
    def get_generic_regression_dataset(
            cls,
            only_continuous_indep: bool = True
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        indep_vars = [Var(var_type=VarType.CONTINUOUS)] * 5
        if not only_continuous_indep:
            indep_vars += [
                Var(var_type=VarType.BINARY),
                Var(var_type=VarType.MULTICLASS, num_of_levels=5)
            ]
        return DatasetsGenerator.get_noise_dataset(
            dep_vars=Var(var_type=VarType.CONTINUOUS),
            indep_vars=indep_vars,
            rows_num=2_000,
            seed=321
        )

    @classmethod
    def get_generic_binary_classification_dataset(
            cls, only_continuous_indep: bool = True
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        indep_vars = [Var(var_type=VarType.CONTINUOUS)] * 5
        if not only_continuous_indep:
            indep_vars += [Var(var_type=VarType.BINARY), Var(var_type=VarType.MULTICLASS, num_of_levels=5)]
        return DatasetsGenerator.get_noise_dataset(
            dep_vars=Var(var_type=VarType.BINARY),
            indep_vars=indep_vars,
            rows_num=2_000,
            seed=321
        )

    @classmethod
    def get_noise_dataset(
            cls,
            dep_vars: Var | list[Var],
            indep_vars: Var | list[Var],
            rows_num: int = 1_000,
            seed: int = 12345
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        if isinstance(dep_vars, Var):
            dep_vars = [dep_vars]
        if isinstance(indep_vars, Var):
            indep_vars = [indep_vars]
        np.random.seed(seed)
        dep_df = cls._get_noise_data(variabs=dep_vars, rows_num=rows_num)
        indep_df = cls._get_noise_data(variabs=indep_vars, rows_num=rows_num)
        dep_df.columns = [f"Y_{k}" for k in range(1, dep_df.shape[1] + 1, 1)]
        indep_df.columns = [f"X_{k}" for k in range(1, indep_df.shape[1] + 1, 1)]
        return indep_df, dep_df

    @classmethod
    def _get_noise_data(cls, variabs: list[Var], rows_num: int) -> pd.DataFrame:
        return pd.DataFrame(
            data=np.concatenate([cls._get_noise(var=var, rows_num=rows_num).reshape(-1, 1) for var in variabs], axis=1))

    @staticmethod
    def _get_noise(var: Var, rows_num: int) -> np.array:
        if var.var_type == VarType.CONTINUOUS:
            return np.random.randn(rows_num)
        else:
            return np.random.randint(1, var.num_of_levels + 1, size=rows_num)

    @classmethod
    def get_linear_regression_dataset(
            cls,
            rows_num: int,
            regressors_num: int,
            informative_regressors_num: int,
            bias: float,
            sigma: float = 10,
            seed: int = 123456
    ) -> tuple[pd.DataFrame, pd.DataFrame, np.array]:
        X, y, coeffs_array = make_regression(
            n_samples=rows_num,
            n_features=regressors_num,
            n_informative=informative_regressors_num,
            n_targets=1,
            bias=bias,
            random_state=seed,
            coef=True,
            noise=sigma
        )
        y = y.reshape(-1, 1)
        X_df = pd.DataFrame(data=X, columns=[f"X_{k}" for k in range(1, regressors_num + 1, 1)])
        y_df = pd.DataFrame(data=y, columns=["y"])
        return X_df, y_df, coeffs_array
