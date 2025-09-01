
import random

def play(choice_str):
    bot = random.choice([-1, 1, 0])

    game_dict = {
        "s": 1,
        "w": -1,
        "g": 0
    }
    reverse_game_dict = {
        1: "snake",
        -1: "water",
        0: "gun"
    }

    # Handle invalid input
    if choice_str not in game_dict:
        return {"error": "Invalid input! Please write w, s or g"}

    user = game_dict[choice_str]

    result = {
        "user_choice": reverse_game_dict[user],
        "bot_choice": reverse_game_dict[bot]
    }

    if bot == user:
        result["outcome"] = "It's a draw 🤝"
    else:
        if bot == -1 and user == 1:
            result["outcome"] = "You win 🎉"
        elif bot == -1 and user == 0:
            result["outcome"] = "You lose 😢"
        elif bot == 1 and user == -1:
            result["outcome"] = "You lose 😢"
        elif bot == 1 and user == 0:
            result["outcome"] = "You win 🎉"
        elif bot == 0 and user == 1:
            result["outcome"] = "You lose 😢"
        elif bot == 0 and user == -1:
            result["outcome"] = "You win 🎉"

    return result
