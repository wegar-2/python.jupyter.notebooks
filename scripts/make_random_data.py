from src.var import Var
from src.var_type import VarType
from src.datasets_generator import DatasetsGenerator


if __name__ == "__main__":

    dep_vars = [Var(var_type=VarType.CONTINUOUS)] * 2
    indep_vars = [Var(var_type=VarType.CONTINUOUS)] * 5

    data = DatasetsGenerator.get_noise_dataset(dep_vars=dep_vars, indep_vars=indep_vars, rows_num=2_000, seed=321)

    print(data)
