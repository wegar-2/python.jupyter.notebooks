from typing import Optional
from pydantic import BaseModel, ConfigDict, PositiveInt
from src.var_type import VarType


class Var(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    var_type: VarType
    num_of_levels: Optional[PositiveInt] = None

