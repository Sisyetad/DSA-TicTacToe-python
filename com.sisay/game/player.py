# game/player.py
from abc import ABC, abstractmethod
from .board import Board
from typing import Tuple

class Player(ABC):
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        pass

    def get_symbol(self) -> str:
        return self.symbol

class HumanPlayer(Player):
    def get_move(self, board: Board) -> Tuple[int, int]:
        while True:
            try:
                move = input(f"Enter your move for {self.symbol} (row and column, 0-2): ")
                row, col = map(int, move.split())

                if not (0 <= row < 3) or not (0 <= col < 3):
                    raise ValueError("Row and column must be between 0 and 2.")

                if board.board[row][col] != ' ':
                    raise ValueError("This position is already occupied. Try a different position.")

                return row, col

            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid row and column numbers.")
            except Exception as e:
                print(f"Unexpected error: {e}. Please try again.")
