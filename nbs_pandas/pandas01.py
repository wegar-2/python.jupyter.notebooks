from string import ascii_uppercase

import numpy as np
import pandas as pd


if __name__ == "__main__":

    data = pd.DataFrame(data={
        "X": np.random.randn(100),
        "categ": np.random.choice(list(ascii_uppercase), size=100, replace=True)
    })
    print(data.head())

    aggs_data = data.groupby("categ")[["X"]].agg({
        "X": [
            ("my_mean", np.mean),
            ("my_median", np.median)
        ]
    })
    aggs_data.columns = [
        '_'.join(col).strip() for col in aggs_data.columns.values
    ]

    # using custom callable
    def my_fun(x):
        return (max(x) + min(x)) / 2

    data.groupby("categ").agg({"X": [("my_aggreg", my_fun)]})
