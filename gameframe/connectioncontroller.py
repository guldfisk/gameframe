import typing as t

from abc import ABC
from multiprocessing.connection import Connection

from gameframe.signature import ObserverSignature


class SignatureConnection(object):

    def __init__(self, signature: ObserverSignature, connection: Connection):
        self._signature = signature
        self._connection = connection


class ConnectionController(ABC):

    def __init__(self, connections: t.Iterable[SignatureConnection]):
        pass
