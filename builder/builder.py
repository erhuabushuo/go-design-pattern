from typing import Protocol

from product import Product1


class Builder(Protocol):
    @property
    def product(self) -> Product1:
        pass

    def produce_part_a(self) -> None:
        pass

    def produce_part_b(self) -> None:
        pass

    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1:
    _product: Product1

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")
