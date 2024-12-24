# Snake and Ladder Game 🎲🐍🪜

A fun and interactive command-line game based on the classic board game **Snake and Ladder**. The goal is to reach position 100 by rolling a dice while avoiding snakes and climbing ladders.

---

## Features
- Roll a dice to move your token.
- Snakes will pull you down to a lower position.
- Ladders will lift you to a higher position.
- Requires rolling a `6` to start the game.
- Displays your current position after every move.

---

## How to Play
1. Run the game in your terminal or IDE.
2. Enter your name when prompted.
3. Press `Enter` to roll the dice.
4. If you land on a ladder, your position increases.
5. If you land on a snake, your position decreases.
6. Reach position `100` to win the game.

---

## Game Rules
- The game starts at position `0`. You must roll a `6` to begin moving.
- Rolling a dice will give a random number between `1` and `6`.
- Snakes and Ladders positions:
  - **Ladders**: Move up
    - `3 → 21`
    - `30 → 44`
    - `12 → 87`
    - `77 → 99`
  - **Snakes**: Move down
    - `16 → 6`
    - `56 → 13`
    - `88 → 63`
    - `98 → 9`
- The first player to reach position `100` wins the game.

---

## Prerequisites
- Python 3.x installed on your system.

---

## How to Run
1. Save the script as `snake_ladder_game.py`.
2. Open a terminal or your preferred Python IDE.
3. Navigate to the directory containing the script.
4. Run the script using:
   ```bash
   python snake_ladder_game.py
