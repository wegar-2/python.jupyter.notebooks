from enum import Enum, auto


class VarType(Enum):
    CONTINUOUS = auto()
    BINARY = auto()
    MULTICLASS = auto()
