import os

class Environment:
    TEST = 'test'

    URLS = {
        TEST: 'https://automationintesting.online/'
    }

    def __init__(self):
        try:
            self.env = os.getenv('ENV')
        except KeyError:
            self.env = self.TEST

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")

host = Environment()