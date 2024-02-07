"""
Demonstration of how dict.setdefault() can be put to use.
"""

import numpy as np


if __name__ == "__main__":

    np.random.seed(12345)
    nums = np.random.randint(1, 1001, size=10_000)

    positions_dict: dict[int, list[int]] = {}

    print("saving positions of given values in dictionary")
    for i, x in enumerate(list(nums)):
        positions_dict.setdefault(x, []).append(i)

    print("displaying the lists of positions by value")
    for num, positions in positions_dict.items():
        print(f"{num}: {positions}")
