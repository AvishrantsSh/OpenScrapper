import requests, json
from bs4 import BeautifulSoup

class Fetcher(object):
    response = ""
    n_response = {}
    def __init__(self, link):
        print("Fetching")
        self.link = link
        Fetcher.response = requests.get(url = self.link)
        print("Done")

    def extract(self):
        soup = BeautifulSoup(self.response.content, 'html5lib')
        self.lst = soup.find_all('table')
        return self.lst

    def jsonify(self, index, order="row"):
        if order == "row":
            keys=[]
            result = {}
            rows = self.lst[index].find_all('tr')
            for i in range(len(rows)):
                element = rows[i].find_all('td')
                for j in range(len(element)):
                    if i == 0:
                        keys.append(element[j].get_text())
            print(keys)

        elif order == "column":
            columns = self.lst[index].find_all('tr')
            print(columns)
            
        else:
            return "Invalid Arguments"
        return "Hola"