from typing import Any


if __name__ == "__main__":

    # ----- (1) .update() method -----
    dict_ = {"a": 1, "b": 3}
    print(dict_)
    dict_.update({"b": 123, "c": 909})
    print(dict_)

    # ----- (2) .pop() Python dict element by key -----
    print(dict_.pop("c"))

    # ----- (3) .popitem() -> (key, value) pairs -----
    print(dict_.popitem())
    print(dict_.popitem())
    print(dict_)

    dict_: dict[Any, Any] = {"v": 15, "b": 909, "f": 300}

    # ----- (4) in operator -----
    print("f" in dict_)

    # ----- (5) .pop() with default value returned -----
    print(dict_.pop("q", "no such element found..."))

    # ----- (6) .get() with default if no value under key -----
    print(dict_.get("q", "some default value"))

    # ----- (7) .setdefault() -----
    print(dict_.setdefault("z", "default value"))
    