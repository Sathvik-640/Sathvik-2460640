#!/usr/bin/env python3
"""
Simple Rock Paper Scissors CLI game.

Run: python rps.py
"""

import random
from typing import Literal, Tuple

Choice = Literal["rock", "paper", "scissors"]


def normalize_choice(raw: str) -> Choice | None:
    """Normalize user input to one of 'rock', 'paper', 'scissors' or return None if invalid."""
    if not raw:
        return None
    s = raw.strip().lower()
    if s in ("r", "rock"):
        return "rock"
    if s in ("p", "paper"):
        return "paper"
    if s in ("s", "scissors", "scissor"):
        return "scissors"
    return None


def get_computer_choice() -> Choice:
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player: Choice, computer: Choice) -> str:
    """
    Determine winner:
    returns "tie", "player", or "computer"
    """
    if player == computer:
        return "tie"
    # rock beats scissors, scissors beats paper, paper beats rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    return "player" if wins[player] == computer else "computer"


def ask_best_of() -> int:
    """Ask the player for a best-of number (must be odd positive integer). Default is 3."""
    while True:
        resp = input("Play best of how many rounds? (odd number, default 3) > ").strip()
        if resp == "":
            return 3
        if resp.isdigit():
            n = int(resp)
            if n > 0 and n % 2 == 1:
                return n
            print("Please enter a positive odd number (e.g., 1, 3, 5...).")
        else:
            print("Please enter a valid number (or press Enter for default).")


def play_round() -> Tuple[str, str, str]:
    """
    Play one round. Returns a tuple (player_choice, computer_choice, result)
    where result is one of "tie", "player", "computer".
    """
    while True:
        raw = input("Your move ([r]ock, [p]aper, [s]cissors or 'q' to quit) > ")
        if raw.strip().lower() == "q":
            raise KeyboardInterrupt  # handled by caller to quit gracefully
        player = normalize_choice(raw)
        if player is None:
            print("Invalid input. Please enter rock, paper, scissors, r, p, or s.")
            continue
        comp = get_computer_choice()
        result = determine_winner(player, comp)
        return player, comp, result


def main():
    print("Welcome to Rock Paper Scissors!")
    try:
        while True:
            best_of = ask_best_of()
            rounds_needed = best_of // 2 + 1
            player_score = 0
            comp_score = 0
            round_number = 1

            while player_score < rounds_needed and comp_score < rounds_needed:
                print(f"\nRound {round_number} — Score: You {player_score} : {comp_score} Computer")
                try:
                    player, comp, result = play_round()
                except KeyboardInterrupt:
                    print("\nQuitting game. Goodbye!")
                    return

                print(f"You chose: {player}. Computer chose: {comp}.")
                if result == "tie":
                    print("It's a tie!")
                elif result == "player":
                    player_score += 1
                    print("You win this round!")
                else:
                    comp_score += 1
                    print("Computer wins this round!")

                round_number += 1

            print(f"\nFinal score — You {player_score} : {comp_score} Computer")
            if player_score > comp_score:
                print("Congratulations, you won the match!")
            else:
                print("Computer won the match. Better luck next time!")

            again = input("\nPlay again? (y/N) > ").strip().lower()
            if again != "y":
                print("Thanks for playing. Goodbye!")
                break

    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
````markdown name=README.md
```markdown
# Rock Paper Scissors — CLI (Python)

A very small command-line Rock Paper Scissors game written in Python.

## Requirements
- Python 3.7+

## Run
1. Make sure you have Python installed.
2. Run the game:
```bash
python rps.py
