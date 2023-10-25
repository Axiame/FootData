import requests


class RequestHandler:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'
        }

    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            print(e)
            return None