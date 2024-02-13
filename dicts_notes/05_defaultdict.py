from collections import defaultdict
import numpy as np
from string import ascii_letters


if __name__ == '__main__':
    dict_ = {"a": 32, "b": 901}
    dd = defaultdict(list)
    nums = np.random.choice(list(ascii_letters), size=1_000, replace=True)

    for i, ltr in enumerate(nums):
        dd[ltr].append(i)

    for ltr, posits in dd.items():
        print(f"{ltr}: {posits}")


