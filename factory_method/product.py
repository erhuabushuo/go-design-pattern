from typing import Protocol


class Product(Protocol):
    def operation(self) -> str:
        pass


class ConcreteProduct1:
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2:
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
