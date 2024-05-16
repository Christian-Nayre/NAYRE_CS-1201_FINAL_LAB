from datetime import datetime

class ScoreManager:
    def __init__(self):
        self.scores = []
        self.leaderboard = []  # para sa mga score
        self.load_scores()

    def add_score(self, username, points):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # para kunen oras ngayon
        self.scores.append((username, points, current_time))
        self.save_scores()  # masasave yung score sa file pagkatapos mag add ng score 
        self.update_leaderboard()  # update lang yung leaderboard

    def save_scores(self):
        with open('scores.txt', 'w') as file:
            for username, points, date_time in self.scores:
                file.write(f"{username},{points},{date_time}\n")

    def load_scores(self):
        try:
            with open('scores.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        username, points, date_time = parts
                        self.scores.append((username, int(points), date_time))
                    elif line.strip():  
                        print(f"Warning: Skipping malformed score data: {line.strip()}")
        except FileNotFoundError:
            open('scores.txt', 'w').close()

    def update_leaderboard(self):
        user_points = {}
        for username, points, date_time in self.scores:
            if username not in user_points or points > user_points[username][0]:
                user_points[username] = (points, date_time)

        self.leaderboard = sorted(user_points.items(), key=lambda x: x[1][0], reverse=True)[:10]

    def print_leaderboard(self):
        self.update_leaderboard() 
        print("Leaderboard:")
        for i, (username, (points, date_time)) in enumerate(self.leaderboard, 1):
            print(f"{i}. Username: {username}, Points: {points}, Date: {date_time}")



