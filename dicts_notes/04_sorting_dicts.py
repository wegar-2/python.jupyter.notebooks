import numpy as np


if __name__ == "__main__":
    rands = np.random.choice(range(100), size=100, replace=False)
    dict_ = dict(zip(rands, range(100)))
    dict_sorted = dict(sorted(dict_.items()))
    print(dict_sorted)
