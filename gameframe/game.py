
from abc import ABC, abstractmethod

from eventtree.replaceevent import EventSession
from gameframe.interface import GameInterface
from gameframe.setupinfo import SetupInfo


class Zone(object):
    pass


class Price(object):
    pass


class Card(object):
    pass


class Game(EventSession):

    def __init__(self, setup_info: SetupInfo, interface: GameInterface):
        super().__init__()
        self._setup_info = setup_info
        self._interface = interface

    @property
    def interface(self) -> GameInterface:
        return self._interface

    @abstractmethod
    def start(self):
        pass