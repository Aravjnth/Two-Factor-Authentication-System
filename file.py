import random
import time
import hashlib

class TwoFactorAuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Error: User already exists")
            return
        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        self.users[username] = {'password': hashed_password, 'salt': salt, '2fa_secret': self.generate_2fa_secret()}
        print(f"User '{username}' registered successfully")

    def generate_salt(self):
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()

    def hash_password(self, password, salt):
        return hashlib.sha256((password + salt).encode()).hexdigest()

    def generate_2fa_secret(self):
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()

    def login(self, username, password):
        if username not in self.users:
            print("Error: User not found")
            return
        user = self.users[username]
        hashed_password = self.hash_password(password, user['salt'])
        if hashed_password != user['password']:
            print("Error: Invalid password")
            return
        print("Password correct. Generating 2FA code...")
        self.send_2fa_code(username)

    def send_2fa_code(self, username):
        user = self.users[username]
        timestamp = int(time.time())
        code = self.generate_2fa_code(user['2fa_secret'], timestamp)
        print(f"2FA code: {code}")
        # Send the code to the user's phone or email

    def generate_2fa_code(self, secret, timestamp):
        return hashlib.sha256((secret + str(timestamp)).encode()).hexdigest()[:6]

    def verify_2fa_code(self, username, code):
        user = self.users[username]
        timestamp = int(time.time())
        expected_code = self.generate_2fa_code(user['2fa_secret'], timestamp)
        if code == expected_code:
            print("2FA code correct. Login successful")
            return True
        print("Error: Invalid 2FA code")
        return False

# Example usage
system = TwoFactorAuthenticationSystem()

system.register_user('Aravinth', 'mysecretpassword')

system.login('Aravinth', 'mysecretpassword')

# User receives the 2FA code and enters it
code = input("Enter 2FA code: ")
system.verify_2fa_code('Aravinth', code)