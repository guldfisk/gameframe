import typing as t

from abc import ABC, abstractmethod


class GameInterface(ABC):

    @abstractmethod
    def select_option(self) -> t.Any:
        pass

    @abstractmethod
    def notify_