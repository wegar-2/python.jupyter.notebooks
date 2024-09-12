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

    # behavior of ChainMap for ties
    cm0 = ChainMap()
    cm0 = cm0.new_child({"a": 43, "b": 9803})
    cm0 = cm0.new_child({"b": 909, "g": 76})
    print(cm0)
    print(cm0["b"]) # note that the later child's value is printed
    cm0.update({"l": 123})
    print(cm0)
