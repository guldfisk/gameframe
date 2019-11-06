
import typing as t

from abc import ABC, abstractmethod

from eventtree.replaceevent import EventSession
from gameframe.interface import GameInterface
from gameframe.setupinfo import SetupInfo
from gameframe.signature import PlayerSignature


class Zone(object):
    pass


class Price(object):
    pass


class Card(object):
    pass


class Game(EventSession):

    def __init__(self, setup_info: SetupInfo, interface: GameInterface, signatures: t.Collection[PlayerSignature]):
        super().__init__()
        self._setup_info = setup_info
        self._interface = interface
        self._signatures = signatures

    @property
    def interface(self) -> GameInterface:
        return self._interface

    @abstractmethod
    def start(self):
        pass