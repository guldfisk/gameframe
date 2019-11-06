from __future__ import annotations

import typing as t

from abc import ABC, abstractmethod, ABCMeta

from eventtree.replaceevent import Event


class GameEventMeta(ABCMeta):

    @staticmethod
    def _get_keyed_prop(key) -> object:
        return property(
            lambda o: o._values.__getitem__(key),
            lambda o, v: (o._values.__setitem__(key, v)),
        )

    def __new__(mcs, name, bases, dct):
        fields = (
            frozenset(dct['__annotations__'].keys())
            if '__annotations__' in dct else
            frozenset()
        )
        for base in bases:
            if issubclass(base, Event) and hasattr(base, '__annotations__'):
                fields |= base.__annotations__.keys()
        for key in fields:
            dct[key] = mcs._get_keyed_prop(key)
        dct['_fields'] = fields
        return super().__new__(mcs, name, bases, dct)


class GameEvent(Event, metaclass=GameEventMeta):

    @property
    def fields(self) -> t.FrozenSet[str]:
        return self._fields

    @abstractmethod
    def payload(self, **kwargs):
        pass

    @abstractmethod
    def serialize(self) -> t.Any:
        pass

    @abstractmethod
    def deserialize(self, s: t.Any) -> GameEvent:
        pass

