from typing import List
from card import Card


class Event:
    def __init__(self, title: str, desc: str, cards: List[Card]) -> None:
        self._title = title
        self._desc = desc
        self._cards = cards

    @property
    def title(self) -> str:
        return self._title

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def cards(self) -> List[Card]:
        return self._cards
