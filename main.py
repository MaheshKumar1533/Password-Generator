import random
import string
import hashlib

class PasswordManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = {
            "password": hashlib.sha256(password.encode()).hexdigest(),
            "passwords": []
        }

    def authenticate_user(self, username, password):
        if username not in self.users:
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.users[username]["password"] == hashed_password

    def add_password(self, username, service_name, password):
        if username not in self.users:
            raise ValueError("User not found")
        self.users[username]["passwords"].append({
            "service_name": service_name,
            "password": password
        })

    def generate_password(self, length=12, complexity=3):
        complexity_level = {
            1: string.ascii_lowercase,
            2: string.ascii_letters + string.digits,
            3: string.ascii_letters + string.digits + string.punctuation
        }
        characters = complexity_level.get(complexity, string.ascii_letters + string.digits + string.punctuation)
        return ''.join(random.choice(characters) for _ in range(length))

    def check_password_strength(self, password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(char.islower() for char in password) and any(char.isupper() for char in password):
            strength += 1
        if any(char.isdigit() for char in password):
            strength += 1
        if any(char in string.punctuation for char in password):
            strength += 1
        return strength

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.create_user("user1", "password1")
    password_manager.create_user("user2", "password2")

    print(password_manager.users)

    print(password_manager.authenticate_user("user1", "password1"))
    print(password_manager.authenticate_user("user2", "password3"))

    password_manager.add_password("user1", "facebook", "password")
    password_manager.add_password("user1", "gmail", "password")
    print(password_manager.users)

    print(password_manager.generate_password(12, 3))
    print(password_manager.check_password_strength("Password123!"))
