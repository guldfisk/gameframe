
from abc import ABC, abstractmethod

from gameframe.setupinfo import SetupInfo


class Zone(object):
    pass


class Price(object):
    pass


class Card(object):
    pass


class Player(object):
    pass



class Game(ABC):

    def __init__(self, setup_info: SetupInfo):
        pass

    @abstractmethod
    def start(self):
        pass