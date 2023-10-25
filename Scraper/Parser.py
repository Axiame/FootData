from bs4 import BeautifulSoup


class Parser:
    def __init__(self, content):
        self.content = content
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def extract_data(self):
        raise NotImplementedError
