import typing as t

from abc import ABC, abstractmethod

from gameframe.connectioncontroller import ConnectionController
from gameframe.events import GameEvent


# class Option(object):
#
#     def __init__(self, option_id, value: t.Any):
#         pass
from gameframe.player import Player


class GameInterface(ABC):

    def __init__(self, controller: ConnectionController):
        self._controller = controller

    @abstractmethod
    def select_option(self, player: Player, options: t.Iterable[t.Any]) -> t.Any:
        pass

    @abstractmethod
    def notify_event_start(self, event: GameEvent):
        pass

    @abstractmethod
    def notify_event_end(self, event: GameEvent):
        pass