import random

VALID_CHOICES = ("rock", "paper", "scissors")


def get_user_choice() -> str:
    while True:
        raw = input("Choose [rock/paper/scissors] (or 'q' to quit): ").strip().lower()

        if raw in ("q", "quit", "exit"):
            return "quit"

        # Allow short aliases
        aliases = {"r": "rock", "p": "paper", "s": "scissors"}
        choice = aliases.get(raw, raw)

        if choice in VALID_CHOICES:
            return choice

        print("Invalid choice. Please type rock, paper, or scissors.")


def get_computer_choice() -> str:
    return random.choice(VALID_CHOICES)


def determine_winner(user: str, computer: str) -> str:
    if user == computer:
        return "draw"
    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return "user" if (user, computer) in wins else "computer"


def play_round(score: dict) -> bool:
    user = get_user_choice()
    if user == "quit":
        return False

    computer = get_computer_choice()
    result = determine_winner(user, computer)

    print(f"\nYou: {user} | Computer: {computer}")

    if result == "draw":
        score["draws"] += 1
        print("Result: Draw 🤝")
    elif result == "user":
        score["wins"] += 1
        print("Result: You win ✅")
    else:
        score["losses"] += 1
        print("Result: You lose ❌")

    print(f"Score → Wins: {score['wins']} | Losses: {score['losses']} | Draws: {score['draws']}\n")
    return True


def main():
    print("Rock Paper Scissors (CLI)")
    print("------------------------")

    score = {"wins": 0, "losses": 0, "draws": 0}

    while True:
        keep_playing = play_round(score)
        if not keep_playing:
            break

        again = input("Play again? [y/n]: ").strip().lower()
        print()
        if again not in ("y", "yes"):
            break

    print("Thanks for playing!")
    print(f"Final Score → Wins: {score['wins']} | Losses: {score['losses']} | Draws: {score['draws']}")


if __name__ == "__main__":
    main()
