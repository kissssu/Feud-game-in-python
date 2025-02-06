# Feud Game (Python)

This is a simple "Family Feud" style game implemented in Python.  The game presents the player with a category and a number of hidden answers. The player has a limited number of guesses to reveal the answers and score points.

## How to Play

1.  Run the Python script (`family_feud.py`).
2.  You will be presented with a list of categories. Choose one.
3.  You'll be told how many answers there are in that category.
4.  You have 5 attempts to guess the answers.
5.  Correct answers earn points.
6.  The game ends when you either guess all the answers or run out of attempts.
7.  Your total score for the round is displayed.
8.  You can choose to play again with a different category.

## Features

*   Multiple categories (car brands, phone brands, places to visit, and you can easily add more).
*   Case-insensitive input (e.g., "toyota" is the same as "Toyota").
*   Limited number of incorrect attempts (5).
*   Clear output formatting.
*   Play again option.

## Planned Enhancements (Maybe)

*   More categories (e.g., movies, sports, animals, etc.).
*   Team play (two teams competing).
*   A "strike" system (3 strikes and a team loses their turn).
*   A "steal" option (if a team doesn't get all the answers, the other team can try to steal).
*   Graphical user interface (GUI) using a library like Tkinter or Pygame.
*   Sound effects.
*   Saving and loading game state.
*   Storing questions and answers in external files (e.g., JSON or CSV).

## Sample Output
```
------------------------------
Choose a category:
1. Top 10 Car Brands
2. Top 5 Phone Brands
3. Top 5 Places to Visit (India)
------------------------------
Enter your choice (1-3): 1
------------------------------
Category: Top 10 Car Brands
There are 10 answers.
------------------------------
Wrong attempts: 0/5. Your guess: toyota 
Correct! Toyota is worth 25 points. 
Wrong attempts: 0/5. Your guess: honda 
Correct! Honda is worth 22 points. 
Wrong attempts: 0/5. Your guess: 
Choose a category:
... (rest of the game)
```

## How to Run

1. Save the code as `main.py`.
2. Make sure you have Python 3 installed.
3. Open a terminal or command prompt.
4. Navigate to the directory where you saved the file.
5. Run the script using: `python main.py`

## Collaboration

Contributions are welcome! Feel free to submit pull requests with improvements, new features, or bug fixes.  You can add more categories, enhance the user interface (e.g., using a library like `Tkinter` or `Pygame`), implement a scoring system for multiple rounds or teams, add sound effects, or improve the game's logic.