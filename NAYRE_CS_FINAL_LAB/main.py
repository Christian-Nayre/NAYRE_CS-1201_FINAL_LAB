from utils.user_manager import UserManager
from utils.dicegame import DiceGame
from utils.score_manager import ScoreManager

def play_game_session(username, score_manager):
    total_points = 0  # points na nakauha every match
    while True:
        print("\nLogged in as:", username)
        print("1. Start Game")
        print("2. See Leaderboard")
        print("3. Log out")

        inner_choice = input("Enter your choice: ")

        if inner_choice == "1":
            while True:
                # Start match
                game = DiceGame()
                phases = game.play_match()
                user_points = 0
                for phase in phases:
                    print("\nPhase:", phase)
                    user_roll, cpu_roll = game.play_game()
                    print(f"Your roll: {user_roll}")
                    print(f"CPU roll: {cpu_roll}")
                    winner = game.winner(user_roll, cpu_roll)
                    if winner == "User":
                        user_points += 1
                    print(f"The winner of the phase is: {winner}")
                
                if user_points >= 2:
                    user_points += 3
                    total_points += user_points
                    print("Congratulations! You won the match!")
                    print("Your total points so far:", total_points)
                else:
                    print("Sorry, you lost the match.")
                    print("Your total points for this match:", user_points)
                
                if input("Do you want to continue playing? (y/n): ").lower() != "y":
                    score_manager.add_score(username, total_points)
                    break

        elif inner_choice == "2":
            # leaderboard
            score_manager.print_leaderboard()

        elif inner_choice == "3":
            # logout
            print("Logging out...")
            score_manager.add_score(username, total_points)
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    user_manager = UserManager()
    score_manager = ScoreManager()
    user_manager.load_users()

    while True:
        print("\nWelcome to the Dice Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # register
            username = input("Enter your username: ")
            password = input("Enter your password (4 characters): ")
            if user_manager.register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists or password must be 4 characters long.")

        elif choice == "2":
            # login
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if user_manager.login_user(username, password):
                print("Login successful!")
                play_game_session(username, score_manager)
            else:
                print("Incorrect username or password.")

        elif choice == "3":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
