import typing as t

import random
import time
import threading

from multiprocessing import Process, Pipe
from typing import Optional, Callable, Any, Iterable, Mapping

from gameframe.connectioncontroller import ConnectionController
from gameframe.game import Game
from gameframe.interface import GameInterface
from gameframe.setupinfo import SetupInfo
from gameframe.signature import ObserverSignature, PlayerSignature


class GameThread(threading.Thread):

    def __init__(self, game: Game) -> None:
        super().__init__(daemon = True)
        self._game = game

    def run(self) -> None:
        self._game.start()



class GameSession(Process):
    
    def __init__(
        self,
        connection_controller_type: t.Type[ConnectionController],
        observer_signatures: t.Iterable[ObserverSignature],
        interface_type: t.Type[GameInterface],
        setup_info: SetupInfo,
        game_type: t.Type[Game],
        seed: t.Optional[t.ByteString] = None,
    ) -> None:
        super().__init__()
        self._observer_signatures = frozenset(observer_signatures)
        self._player_signatures = frozenset(
            signature
            for signature in
            self._observer_signatures
            if isinstance(signature, PlayerSignature)
        )

        self._connection_controller = connection_controller_type(self._observer_signatures)

        self._interface = interface_type(self._connection_controller)
        self._setup_info = setup_info
        self._game: Game = game_type(self._setup_info, self._interface)
        self._seed: t.ByteString = (
            str(hash(time.time())).encode('ASCII')
            if seed is None else
            seed
        )

    def run(self):
        random.seed(self._seed)
        self._game.start()