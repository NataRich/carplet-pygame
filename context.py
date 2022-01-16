import json
import os
from typing import List

from index import Index
from event import Event
from card import Card


class Context:
    def __init__(self, file: str) -> None:
        if not os.path.isfile(file):
            raise FileNotFoundError("Expected a file but found none")

        if os.path.splitext(file)[1] != ".json":
            raise FileNotFoundError("Expected a json file but found none")

        with open(file, 'r') as f:
            self._data = json.load(f)

        self._name: str = ""
        self._success: str = ""
        self._creator: str = ""
        self._indexes: List[Index] = []
        self._plots: List[List[Event]] = []
        self._plot_count = 0
        self._event_count = 0

        self.__extract()
        self.__validated()

    @property
    def name(self) -> str:
        return self._name

    @property
    def creator(self) -> str:
        return self._creator

    @property
    def success(self) -> str:
        return self._success

    @property
    def indexes(self) -> List[Index]:
        return self._indexes

    @property
    def plots(self) -> List[List[Event]]:
        return self._plots

    def curr_event(self) -> Event or None:
        if not self.plot_finished():
            return self._plots[self._plot_count][self._event_count]
        return None

    def next_event(self) -> None:
        if not self.plot_finished():
            self._event_count += 1

    def curr_plot(self) -> List[Event]:
        if not self.context_finished():
            return self._plots[self._plot_count]
        return []

    def next_plot(self) -> None:
        if not self.context_finished():
            self._plot_count += 1
            self._event_count = 0  # events start from beginning

    def is_game_over(self) -> bool:
        for i in self._indexes:
            if i.destroy():
                return True
        return False

    def cause_index(self) -> int:
        for key, i in enumerate(self._indexes):
            if i.destroy():
                return key
        return -1

    def plot_finished(self) -> bool:
        return self._event_count >= len(self._plots[self._plot_count])

    def context_finished(self) -> bool:
        return self._plot_count >= len(self._plots)

    def reset(self) -> None:
        self._plot_count = 0
        self._event_count = 0
        for i in self._indexes:
            i.reset()
        self.__validated()

    def __extract(self) -> None:
        self._name = self._data['name']
        self._creator = self._data['creator']
        self._success = self._data['success']

        for raw_index in self._data['indexes']:
            self._indexes.append(Index(raw_index['name'], raw_index['start'], raw_index['asset'], raw_index['end']))

        for raw_events in self._data['plots']:
            events = []
            for raw_event in raw_events:
                cards = []
                for raw_card in raw_event['cards']:
                    cards.append(Card(raw_card['title'], raw_card['desc'], raw_card['effects'], raw_card['cons']))
                events.append(Event(raw_event['title'], raw_event['desc'], cards))
            self._plots.append(events)

    def __validated(self) -> None:
        if self._name == "":
            raise ValueError("Name of the game cannot be empty string")

        if self._creator == "":
            raise ValueError("Name of the creator cannot be be empty string")

        if self._success == "":
            raise ValueError("Success string cannot be be empty")

        if len(self._indexes) != 4:
            raise ValueError("Number of indexes must be equal to 4")

        for index in self._indexes:
            if index.end_str == "":
                raise ValueError("End string of index cannot be be empty")

        if len(self._plots) == 0:
            raise ValueError("Number of plots must be greater than 0")

        for plot in self._plots:
            if len(plot) == 0:
                raise ValueError("Number of events in one plot must be greater than 0")
            for event in plot:
                if event.title == "":
                    raise ValueError("Event title cannot be empty string")
                if event.desc == "":
                    raise ValueError("Event description cannot be empty string")
                if len(event.cards) != 3:
                    raise ValueError("Number of cards must be equal to 3")
                for card in event.cards:
                    if card.title == "":
                        raise ValueError("Card title cannot be empty string")
                    if card.desc == "":
                        raise ValueError("Card description cannot be empty string")
                    if card.cons == "":
                        raise ValueError("Card consequence cannot be empty string")
                    if len(card.effects) != len(self._indexes):
                        raise ValueError("Number of effects should be equal to number of indexes")

