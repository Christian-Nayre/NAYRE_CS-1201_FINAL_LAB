class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password_length(self):
        return len(self.password) == 4