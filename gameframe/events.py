from __future__ import annotations

import typing as t

from abc import ABC, abstractmethod

from eventtree.replaceevent import Event


class GameEvent(Event, ABC):

    @abstractmethod
    def payload(self, **kwargs):
        pass

    @abstractmethod
    def serialize(self) -> t.Any:
        pass

    @abstractmethod
    def deserialize(self, s: t.Any) -> GameEvent:
        pass