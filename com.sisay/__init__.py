from game.board import Board
from game.player import HumanPlayer
from game.ai_player import AIPlayer

class TicTacToeGame:
    def __init__(self, player1: HumanPlayer, player2: AIPlayer, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_player = player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        while True:
            self.board.display()
            try:
                move = self.current_player.get_move(self.board)
                if not self.board.update(move, self.current_player.get_symbol()):
                    raise ValueError("Invalid move. The cell is already occupied.")

                winner = self.board.check_winner()
                if winner:
                    self.board.display()
                    print(f"Player {winner} wins!")
                    break

                if self.board.is_full():
                    self.board.display()
                    print("It's a draw!")
                    break

                self.switch_player()

            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    player1 = HumanPlayer('X')
    player2 = AIPlayer('O', 'X')
    board = Board()
    game = TicTacToeGame(player1, player2, board)
    game.play()