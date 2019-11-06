from eventtree.replaceevent import SessionBound, EventSession
from gameframe.signature import PlayerSignature


class Player(SessionBound):

    def __init__(self, session: EventSession, signature: PlayerSignature):
        super().__init__(session)
        self._signature = signature
