from typing import Optional
from pydantic import BaseModel, ConfigDict, PositiveInt, model_validator
from src.var_type import VarType


class Var(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    var_type: VarType
    num_of_levels: Optional[PositiveInt] = None

    @model_validator(mode="before") # noqa
    @classmethod
    def _validate_discrete_var(cls, values):
        if values["var_type"] == VarType.BINARY:
            values["num_of_levels"] = 2
        if values["var_type"] == VarType.MULTICLASS and values["num_of_levels"] <= 2:
            raise ValueError("Incorrect number of levels of multiclass variable detected! "
                             "Number of levels of multiclass variable has to be at least 3! ")
        return values
