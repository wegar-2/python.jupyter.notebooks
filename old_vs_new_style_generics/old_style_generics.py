from typing import TypeVar, Generic, TypeAlias
from functools import reduce
from operator import mul


T = TypeVar("T")
N = TypeVar("N", bound=[float, int])

Numbers: TypeAlias = list[float] | list[int] | tuple[float, ...] | tuple[int, ...]


def print_elements(l_: list[T]):
    for x in l_:
        print(x)


def my_sum(x: list[N]) -> N:
    return sum(x)


def my_product(x: Numbers) -> float:
    return float(reduce(mul, x))


class Point2d(Generic[T]):

    def __init__(self, x: N, y: N):
        self._x: N = x
        self._y: N = y

    @property
    def x(self) -> N:
        return self._x

    @property
    def y(self) -> N:
        return self._y

    @x.setter
    def x(self, x: N):
        self._x = x

    @y.setter
    def y(self, y: N):
        self._y = y


if __name__ == "__main__":

    i_list = [1, 3, 2]
    f_list = [1.2, 4.39, 7.201]

    print_elements(l_=i_list)
    print_elements(l_=f_list)

    i_sum = my_sum(x=i_list)
    f_sum = my_sum(x=f_list)
    print(f"{i_sum=}")
    print(f"{f_sum=}")

    i_prod = my_product(x=i_list)
    f_prod = my_product(x=f_list)
    print(f"{i_prod=}")
    print(f"{f_prod=}")
