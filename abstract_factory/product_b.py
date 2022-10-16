from abc import ABC, abstractmethod

from product_a import AbstractProductA


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> None:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> None:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
