from typing import List


class Card:
    def __init__(self, title: str, desc: str, effects: List[int], cons: str) -> None:
        if title == "":
            raise ValueError("Card title cannot be empty string")
        if desc == "":
            raise ValueError("Card description cannot be empty string")
        if cons == "":
            raise ValueError("Card consequence cannot be empty string")

        self._title = title
        self._desc = desc
        self._effects = effects
        self._cons = cons

    @property
    def title(self) -> str:
        return self._title

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def effects(self) -> List[int]:
        return self._effects

    @property
    def cons(self) -> str:
        return self._cons
