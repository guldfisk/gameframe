import typing as t

from gameframe.connectioncontroller import ConnectionController
from gameframe.events import GameEvent
from gameframe.interface import GameInterface, O
from gameframe.player import Player


selection = t.Union[O, t.List[O]]


class UndoGameInterface(GameInterface):

    def __init__(self, controller: ConnectionController, wrapping: GameInterface):
        super().__init__(controller)
        self._wrapping = wrapping

        self._selections: t.List[selection] = []

    def select_option(self, player: Player, options: t.Iterable[O]) -> O:
        pass

    def select_options(
        self,
        player: Player,
        options: t.Iterable[O],
        minimum: int = 0,
        maximum: t.Optional[int] = None,
    ) -> t.List[O]:
        pass

    def notify_event_start(self, event: GameEvent):
        pass

    def notify_event_end(self, event: GameEvent, success: bool):
        pass