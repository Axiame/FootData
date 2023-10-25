class DatabaseHandler:
    def __init__(self):
        self.data = []

    def save(self, house):
        self.data.append(house)