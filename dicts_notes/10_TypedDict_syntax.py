from typing import TypedDict


class Car(TypedDict):
    maker: str
    price: int


if __name__ == "__main__":

    employee1 = {"name": "Asdf", "salary": 1234}
    employee2 = {"name": "Qwerty", "salary": 2345}

    EmployeeEntry = TypedDict("EmployeeEntry", {
        "name": str, "salary": float | int
    })

    employee3: EmployeeEntry = {
        "name": 1234,  # marks the inconsistency in IDE: expected str
        "salary": 32
    }

    car: Car = {"maker": "Toyota", "price": 1234}
    print(car)
