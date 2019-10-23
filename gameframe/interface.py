import typing as t

from abc import ABC, abstractmethod

from gameframe.connectioncontroller import ConnectionController
from gameframe.events import GameEvent


class GameInterface(ABC):

    def __init__(self, controller: ConnectionController):
        self._controller = controller

    @abstractmethod
    def select_option(self) -> t.Any:
        pass

    @abstractmethod
    def notify_event(self, event: GameEvent):
        pass