<!DOCTYPE html>
<html lang="en">
<body>
    <div class="container">
        <h1>Tic-Tac-Toe Game</h1>
        <h2>Description</h2>
        <p>
            This project is a Python implementation of the classic Tic-Tac-Toe game, featuring both human and AI players. The AI player is powered by dynamic programming techniques to make optimal decisions, ensuring a challenging experience for players.
        </p>
        <h2>Features</h2>
        <ul>
            <li><strong>Human vs AI</strong>: Play against a computer opponent with advanced AI.</li>
            <li><strong>AI Algorithms</strong>: Utilizes dynamic programming to calculate the best possible move.</li>
            <li><strong>Modular Design</strong>: The code is organized into packages and modules, making it easy to extend and maintain.</li>
            <li><strong>Exception Handling</strong>: Robust error handling for invalid inputs and game state errors.</li>
        </ul>
        <h2>Technologies Used</h2>
        <p>
            <strong>Python</strong>: The entire game is implemented in Python.<br>
            <strong>Dynamic Programming</strong>: Used in the AI's decision-making process.
        </p>
        <h2>Project Structure</h2>
        <div class="structure">
            tic_tac_toe/<br>
            ├── game/<br>
            │   ├── __init__.py<br>
            │   ├── board.py         # Contains the Board class managing the game state.<br>
            │   ├── player.py        # Defines the abstract Player class and HumanPlayer class.<br>
            │   ├── ai_player.py     # Implements the AIPlayer class using dynamic programming.<br>
            |   ├── ui
            |        ├── gui.py
            ├── main.py              # Main script to run the Tic-Tac-Toe game.<br>
            └── __init__.py<br>
        </div>
        <h2>Game Components</h2>
        <ul>
            <li><strong>Board Class</strong>: Manages the game board, including moves, checking for a winner, and displaying the board.</li>
            <li><strong>Player Class (Abstract)</strong>: Defines the interface for all players. Both human and AI players inherit from this class.</li>
            <li><strong>HumanPlayer Class</strong>: Handles moves made by a human player.</li>
            <li><strong>AIPlayer Class</strong>: Implements the game-playing AI using dynamic programming to decide optimal moves.</li>
        </ul>
        <h2>How to Run the Game</h2>
        <div class="commands">
            1. <strong>Clone the repository:</strong><br>
            <code>git clone https://github.com/your-username/tic-tac-toe.git</code><br><br>
            2. <strong>Navigate to the project directory:</strong><br>
            <code>cd tic_tac_toe</code><br><br>
            3. <strong>Run the game:</strong><br>
            <code>python main.py</code><br><br>
            4. <strong>Gameplay Instructions:</strong><br>
            - The game will prompt Player X (Human) to input their move by entering the row and column numbers (0-2) separated by a space.<br>
            - The AI (Player O) will automatically make its move after the human player.
        </div>
        <h2>Example Gameplay</h2>
        <pre>
Enter your move for X (row and column, 0-2): 0 0
 X |   |  
-----------
   |   |  
-----------
   |   |  
player O : 1 1
 X |   |  
-----------
   | O |  
-----------
   |   |  
        </pre>
        <h2>Future Improvements</h2>
        <ul>
            <li><strong>Multiplayer Support</strong>: Allow two human players to compete against each other.</li>
            <li><strong>Improved AI</strong>: Implement more sophisticated algorithms like Minimax with Alpha-Beta pruning.</li>
            <li><strong>GUI Version</strong>: Develop a graphical user interface for the game using a framework like Tkinter or Pygame.</li>
        </ul>
        <h2>License</h2>
        <p>
            This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.
        </p>
        <footer>
            &copy; 2024 Your Name. All rights reserved.
        </footer>
    </div>
</body>
</html>
