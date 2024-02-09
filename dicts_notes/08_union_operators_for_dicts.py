

if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 23, "c": 22}

    # (1) via logical symbol of OR
    dict_ = dict1 | dict2
    print(f"{dict1=}")
    print(f"{dict2=}")
    print(f"{dict_=}")

    # (2) via unpacking
    dict_ = {**dict1, **dict2}
    print(f"{dict_=}")

    # (3) using the in-place .update method
    dict_ = dict1
    dict_.update(dict2)
    print(f"{dict_=}")
