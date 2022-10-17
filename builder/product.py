class Product1:
    parts: list[str]

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts:{', '.join(self.parts)}")
