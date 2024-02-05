import random
from typing import TypeVar, TypeAlias

words = ["qwerty", "asdf", "poiuy"]

T = TypeVar("T")
CollT: TypeAlias = list[T] | tuple[T, ...]

type CollN = list[N] | tuple[N, ...] # noqa


def old_choice(x: CollT):
    return random.choice(x)


def new_choice(x: CollN):
    return random.choice(x)


if __name__ == "__main__":

    print(old_choice(x=words))
    print(new_choice(x=words))
