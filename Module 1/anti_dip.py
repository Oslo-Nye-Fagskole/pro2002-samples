class FileLogger:
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")


class Shop:
    def __init__(self):
        self.items = []
        self.logger = FileLogger()  # Direct dependency on low-level detail

    def add(self, item):
        self.items.append(item)
        self.logger.log(f"Added {item}")  # Business logic tied to FileLogger