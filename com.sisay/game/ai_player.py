# game/ai_player.py
from .player import Player
from .board import Board
from typing import Tuple

class AIPlayer(Player):
    def __init__(self, symbol: str, opponent_symbol: str) -> None:
        super().__init__(symbol)
        self.opponent_symbol = opponent_symbol
        self.dp_cache = {}  # Caches the results of board states

    def dp_minimax(self, board: Board, is_maximizing: bool) -> int:
        state = board.get_state()
        if state in self.dp_cache:
            return self.dp_cache[state]

        winner = board.check_winner()
        if winner == self.symbol:
            return 1
        elif winner == self.opponent_symbol:
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for position in board.get_empty_positions():
                board.set_position(position, self.symbol)
                score = self.dp_minimax(board, False)
                board.reset_position(position)
                best_score = max(best_score, score)
            self.dp_cache[state] = best_score
            return best_score
        else:
            best_score = float('inf')
            for position in board.get_empty_positions():
                board.set_position(position, self.opponent_symbol)
                score = self.dp_minimax(board, True)
                board.reset_position(position)
                best_score = min(best_score, score)
            self.dp_cache[state] = best_score
            return best_score

    def get_move(self, board: Board) -> Tuple[int, int]:
        best_score = float('-inf')
        best_move = None
        for position in board.get_empty_positions():
            board.set_position(position, self.symbol)
            score = self.dp_minimax(board, False)
            board.reset_position(position)
            if score > best_score:
                best_score = score
                best_move = position
        return best_move
