import requests, json
from bs4 import BeautifulSoup

class Fetcher(object):
    response = ""
    n_response = {}
    def __init__(self, link):
        self.link = link
        Fetcher.response = requests.get(url = self.link)

    def extract(self):
        soup = BeautifulSoup(self.response.content, 'html5lib')
        lst = soup.find_all('table')
        return lst