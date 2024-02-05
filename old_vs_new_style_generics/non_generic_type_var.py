import random
from typing import TypeVar


OT = TypeVar("OT")
ON = TypeVar("ON", bound=[float, int])
type NN = float | int # noqa


def old_my_sum(x: list[ON]) -> ON:
    return sum(x)


def old_get_random_element(x: list[OT]) -> OT:
    return random.choice(x)


def new_my_sum(x: list[NN]) -> NN:
    return sum(x)


def new_get_random_element[N](x: list[N]) -> N: # noqa
    return random.choice(x)


if __name__ == "__main__":

    i_list = [1, 4, 3, 9]
    f_list = [1.23, 4.3, 9.3]

    print(old_my_sum(i_list))
    print(old_my_sum(f_list))

    print(new_my_sum(i_list))
    print(new_my_sum(f_list))

    print(old_get_random_element(x=i_list))
    print(old_get_random_element(x=f_list))

    print(new_get_random_element(x=i_list))
    print(new_get_random_element(x=f_list))
