# game/board.py
from typing import Tuple, List

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self) -> None:
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def update(self, position: Tuple[int, int], symbol: str) -> bool:
        if self.board[position[0]][position[1]] == ' ':
            self.board[position[0]][position[1]] = symbol
            return True
        return False

    def is_full(self) -> bool:
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def check_winner(self) -> str:
        lines = self.board + list(zip(*self.board)) + [[self.board[i][i] for i in range(3)], [self.board[i][2-i] for i in range(3)]]
        for line in lines:
            if line[0] == line[1] == line[2] and line[0] != ' ':
                return line[0]
        return ''

    def get_empty_positions(self) -> List[Tuple[int, int]]:
        empty_positions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    empty_positions.append((i, j))
        return empty_positions

    def set_position(self, position: Tuple[int, int], symbol: str) -> None:
        self.board[position[0]][position[1]] = symbol

    def reset_position(self, position: Tuple[int, int]) -> None:
        self.board[position[0]][position[1]] = ' '

    def get_state(self) -> str:
        return ''.join(''.join(row) for row in self.board)
