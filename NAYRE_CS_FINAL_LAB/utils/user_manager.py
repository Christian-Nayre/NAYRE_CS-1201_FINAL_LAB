from utils.user import User

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        if self.is_username_available(username):  
            new_user = User(username, password)
            if new_user.check_password_length():
                self.users.append(new_user)
                self.save_users()
                return True
            else:
                return False
        else:
            return False

    def is_username_available(self, username):
        return not any(user.username == username for user in self.users)

    def save_users(self):
        with open('users.txt', 'w') as file:
            for user in self.users:
                file.write(f"{user.username},{user.password}\n")

    
    def load_users(self):
        try:
            with open('users.txt', 'r') as file:
                lines = file.readlines()
                for line_num, line in enumerate(lines, 1):
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        username, password = parts
                        self.users.append(User(username, password))
                    elif line.strip():  
                        print(f"Warning: Skipping malformed user data in line {line_num}: {line.strip()}")
        except FileNotFoundError:
            pass

    def login_user(self, username, password):
        return any(user.username == username and user.password == password for user in self.users)
