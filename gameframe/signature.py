
from abc import ABC, abstractmethod


class GameObserver(ABC):
    pass


class ObserverSignature(ABC):

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass


class PlayerSignature(ObserverSignature):

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass