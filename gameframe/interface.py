from __future__ import annotations

import typing as t
import functools

from abc import ABC, abstractmethod

from gameframe.connectioncontroller import ConnectionController
from gameframe.events import GameEvent
from gameframe.player import Player


@functools.total_ordering
class Option(object):

    def __init__(self, option_type: str, value: str, item: t.Any = None):
        self._option_type = option_type
        self._value = value
        self._item = item

    @property
    def option_type(self) -> str:
        return self._option_type

    @property
    def value(self) -> str:
        return self._value

    @property
    def item(self) -> t.Any:
        return self._item

    def __hash__(self):
        return hash((self._option_type, self._value))

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self._option_type == other._option_type
            and self._value == other._value
        )

    def __gt__(self, other: Option):
        if self._option_type == other._option_type:
            return self._value > other._value
        return self._option_type > other._option_type


O = t.TypeVar('O', bound = Option)


class GameInterface(ABC):

    def __init__(self, controller: ConnectionController):
        self._controller = controller

    def select_string(self, player: Player, option_type: str, strings: t.Iterable[str]) -> str:
        return self.select_option(
            player,
            (
                Option(
                    option_type,
                    s
                )
                for s in
                set(strings)
            ),
        ).value

    @abstractmethod
    def select_option(self, player: Player, options: t.Iterable[O]) -> O:
        pass

    @abstractmethod
    def select_options(
        self,
        player: Player,
        options: t.Iterable[O],
        minimum: int = 0,
        maximum: t.Optional[int] = None,
    ) -> t.List[O]:
        pass

    # def select_items(
    #     self,
    #     player: Player,
    #     options: t.Iterable[t.Any],
    #     minimum: int = 0,
    #     maximum: t.Optional[int] = None,
    # ) -> t.Iterable[O]:
    #     return self.select_options(
    #         player,
    #         options,
    #         minimum,
    #         maximum,
    #     )

    @abstractmethod
    def notify_event_start(self, event: GameEvent):
        pass

    @abstractmethod
    def notify_event_end(self, event: GameEvent, success: bool):
        pass