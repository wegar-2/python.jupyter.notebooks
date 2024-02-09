""" ChainMap - from doc:
A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit.
It is often much faster than creating a new dictionary and running multiple update() calls.
The class can be used to simulate nested scopes and is useful in templating.

Source: https://docs.python.org/3/library/collections.html#collections.ChainMap
"""

import numpy as np
import pandas as pd
from collections import ChainMap


if __name__ == "__main__":

    dict1 = {"a": 1, "b": 434}
    dict2 = {"c": 44412, "d": 9078}
    cm = ChainMap(dict1, dict2)
    print(f"{cm=}")

    c = ChainMap()
    cc = c.new_child({"a": 1})
    print(f"{c=}")
    print(f"{cc=}")
