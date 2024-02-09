from typing import Any
from string import ascii_uppercase


if __name__ == "__main__":

    dict_: dict[Any, Any] = {"a": 123, "b": 43.5, "g": "rtd"}

    # ----- (1) dict.fromkeys() method -----
    print(dict.fromkeys(list(ascii_uppercase[:5]), 1234))

    # ----- (2) iterating over dict in reverse order -----
    for k, v in reversed(dict_.items()):
        print(f"{k}: {v}")
