class UserManager:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_user(self):
        print(f"Saving user {self.username} to database")

    def send_welcome_email(self):
        print(f"Sending welcome email to {self.email}")

    def generate_report(self):
        print(f"User report for {self.username}")
