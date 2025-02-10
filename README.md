# Feud Game (Python)

This is a "Family Feud" style game implemented in Python. The game presents the player with a category and a number of hidden answers. The player has a limited number of incorrect attempts to reveal the answers and score points.

## How to Run (from GitHub)

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/kissssu/Feud-game-in-python.git
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd Feud-game-in-python
    ```
3.  **Make the script executable (if necessary/optional):**
    ```bash
    chmod +x main.py  # Only if main.py doesn't have execute permissions
    ```
4.  **Run the script:**
    ```bash
    python main.py
    ```

## How to Play

1.  Run the Python script (`main.py`).
2.  You will be presented with a list of categories. Choose one.
3.  You'll be told how many answers there are in that category.
4.  You have 5 attempts to guess the answers.
5.  Correct answers earn points.
6.  The game ends when you either guess all the answers or run out of attempts.
7.  Your total score for the round is displayed, along with the answers you guessed, the answers you missed, and any answers you revealed using points.
8.  You can choose to play again with a different category.

## Features

*   Multiple categories (see the `game_data` dictionary in the code for the current categories. You can easily add more).
*   Case-insensitive input (e.g., "toyota" is the same as "Toyota").
*   Limited number of incorrect attempts (5).
*   **Reveal Feature:** You can spend points to reveal answers. The cost is 5 points per word in the answer. Type `reveal <number>` (e.g., `reveal 3`) to reveal a specific answer.
*   Clear and well-formatted output, including a header that displays the category, answers left, score, and attempts left.
*   Displays guessed answers, missed answers, and revealed answers at the end of each round.
*   Play again option.

## Sample Output

**Category Selection:**
```
----------------------------------------
Choose a category:
1. Things that are Red
2. Foods that Start with the Letter 'P'
3. Animals that Live in the Jungle
4. Ice Cream Flavors
5. Fruits
----------------------------------------
Enter your choice (1-5): 2
```

**Gameplay - Turn:**
```
Category:       Foods that Start with the Letter 'P'
Answers left:   6
Score:          40
Attempts left:  5
----------------------------------------
Correct Answers:
1. Pizza
2. Pasta
3. ______ 
4. _______ 
5. Pineapple
6. _____ 
7. ______ 
8. Pear
9. ___________ 
10. _______ 
----------------------------------------
Your guess (or 'reveal <number>' to reveal an answer): reveal 10
```

**Gameplay - Reveal and End:**
```
----------------------------------------
Category:       Foods that Start with the Letter 'P'
Answers left:   0
Score:          35
Attempts left:  0
----------------------------------------
----------------------------------------
Game over! Total score for Foods that Start with the Letter 'P': 35

All Answers:
- Pizza
- Pasta
- Potato
- Pancake
- Pineapple
- Pecan
- Peanut
- Pear
- Pomegranate
- Pumpkin
----------------------------------------
Do you want to play again? (yes/no): yes
```

## How to Run

1.  Save the code as `main.py`.
2.  Make sure you have Python 3 installed.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using: `python3 main.py`

## Planned Enhancements (Maybe)

*   **Expanded Categories:** Add more categories to the `game_data` to keep the game fresh and exciting.  Think beyond the current set – movies, music, history, science, geography, or even niche interests!
*   **Enhanced Reveal System:** Explore different ways to reveal answers, perhaps offering tiered hints or clues at varying costs.
*   **Visual Appeal:**  Improve the terminal output's aesthetics with color coding, better formatting, or even simple animations.
*   **Score Tracking:** Implement a way to track high scores or store player progress across multiple games.
*   **External Data:**  Consider storing the questions and answers in external files (like JSON or CSV) to make it easier to add and manage content.

## Contributing

Contributions are welcome!  Feel free to submit pull requests with improvements, new features, or bug fixes.  Here are some ideas:

*   **More Categories:** Add more categories to the `game_data` dictionary to expand the game's content.
*   **Enhanced User Interface:** Explore using a GUI library like Tkinter or Pygame to create a more visually appealing interface.
*   **Multiplayer Mode:**  Implement a multiplayer mode where two or more players can compete against each other.
*   **Advanced Scoring:**  Develop a more complex scoring system, perhaps with bonus points for speed or consecutive correct answers.
*   **Sound Effects and Music:** Add sound effects and background music to enhance the game experience.
*   **Data Persistence:** Implement a way to save and load game progress or high scores.
*   **Category Difficulty:** Introduce difficulty levels for categories, affecting the point values or the number of allowed attempts.
