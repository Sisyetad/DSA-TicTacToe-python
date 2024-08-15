# ui/gui.py
import tkinter as tk
from tkinter import messagebox
from game.board import Board
from game.player import HumanPlayer
from game.ai_player import AIPlayer
from typing import Tuple

class TicTacToeGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = Board()
        self.player1 = HumanPlayer('X')
        self.player2 = AIPlayer('O', 'X')
        self.current_player = self.player1

        self.buttons = [[tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2, command=lambda r=r, c=c: self.on_click(r, c)) for c in range(3)] for r in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)

    def on_click(self, row: int, col: int):
        if self.board.board[row][col] == ' ' and self.current_player == self.player1:
            self.board.update((row, col), self.player1.get_symbol())
            self.buttons[row][col].config(text=self.player1.get_symbol())
            if self.check_winner():
                return
            self.current_player = self.player2
            self.ai_move()

    def ai_move(self):
        move = self.player2.get_move(self.board)
        if move:
            self.board.update(move, self.player2.get_symbol())
            row, col = move
            self.buttons[row][col].config(text=self.player2.get_symbol())
            self.check_winner()
            self.current_player = self.player1

    def check_winner(self) -> bool:
        winner = self.board.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()
            return True
        if self.board.is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        self.board = Board()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=' ')
        self.current_player = self.player1

def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
