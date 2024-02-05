from typing import TypeVar, Generic

T = TypeVar("T")


class OldStyle(Generic[T]):

    def __init__(self, x: T):
        self._x: T = x

    def get(self) -> T:
        return self._x


class NewStyle[N]: # noqa

    def __init__(self, x: N):
        self._x: N = x

    def get(self) -> N:
        return self._x


if __name__ == "__main__":

    os_obj = OldStyle(x="asdf")
    print(os_obj.get())

    ns_obj = NewStyle(x="qweryty")
    print(ns_obj.get())
