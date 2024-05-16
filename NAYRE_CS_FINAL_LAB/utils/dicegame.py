import random

class DiceGame:
    def play_game(self):
        user_roll = random.randint(1, 6)
        cpu_roll = random.randint(1, 6)
        return user_roll, cpu_roll

    def play_match(self):
        return ["1", "2", "3"]  # number nung phases kada match

    def winner(self, user_roll, cpu_roll):
        if user_roll > cpu_roll:
            return "User"
        elif user_roll < cpu_roll:
            return "CPU"
        else:
            return "Tie"
