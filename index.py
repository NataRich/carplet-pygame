import os.path


class Index:
    def __init__(self, name: str, start: int, icon: str, end_str: str) -> None:
        if name == "":
            raise ValueError("Index name cannot be empty string")
        self._name = name

        if start <= 0:
            raise ValueError("Index start value cannot be negative or zero")
        self._start = start
        self._value = start

        if not os.path.exists(icon):
            raise ValueError("Index icon path cannot be empty string")
        self._icon = icon

        if end_str == "":
            raise ValueError("Index finish string cannot be empty string")
        self._end_str = end_str

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, d: int) -> None:
        self._value += d

    @property
    def icon(self) -> str:
        return self._icon

    @property
    def end_str(self) -> str:
        return self._end_str

    def reset(self) -> None:
        self._value = self._start
    
    def destroy(self) -> bool:
        return self._value <= 0


    