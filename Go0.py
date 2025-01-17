#!/usr/local/bin/python3
# /usr/bin/python3
# Set the path to your python3 above

#!/usr/bin/python3
# Set the path to your python3 above



from gtp_connection import GtpConnection
from board_base import DEFAULT_SIZE, GO_POINT, GO_COLOR
from board import GoBoard
from board_util import GoBoardUtil
from engine import GoEngine
import signal
import time


class Go0:
    def __init__(self):
        """
        Go player that selects moves randomly from the set of legal moves.
        Does not use the fill-eye filter.
        Passes only if there is no other legal move.

        Parameters
        ----------
        name : str
            name of the player (used by the GTP interface).
        version : float
            version number (used by the GTP interface).
        """
        signal.signal(signal.SIGALRM, self.timeout_handler)
        GoEngine.__init__(self, "Go0", 1.0)

    def timeout_handler(self,signum,frame):
        raise TimeoutError()

    def get_move(self, board: GoBoard, color: GO_COLOR) -> GO_POINT:
        try:
            signal.alarm(self.timelimit)
            move=GoBoardUtil.generate_random_move(board, color, 
                                                use_eye_filter=False)
            signal.alarm(0)
        except TimeoutError:
            return None
        return move

    
  
def run() -> None:
    """
    start the gtp connection and wait for commands.
    """
    board: GoBoard = GoBoard(DEFAULT_SIZE)
    con: GtpConnection = GtpConnection(Go0(), board)
    con.start_connection()


if __name__ == "__main__":
    run()
