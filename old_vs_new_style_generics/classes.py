from typing import TypeVar, Generic

T = TypeVar("T")


class OldGenericClass(Generic[T]):

    def __init__(self, x: T):
        self._x: T = x

    def get(self) -> T:
        return self._x

    def set(self, x: T):
        self._x = x


class NewGenericClass[N]: # noqa

    def __init__(self, x: N):
        self._x: N = x

    def get(self) -> N:
        return self._x

    def set(self, x: N):
        self._x = x


if __name__ == "__main__":

    old_obj = OldGenericClass(x=123)
    print(old_obj.get())
    old_obj.set(x=324)
    print(old_obj.get())

    new_obj = NewGenericClass(x=980)
    print(new_obj.get())
    new_obj.set(x=2221)
    print(new_obj.get())
