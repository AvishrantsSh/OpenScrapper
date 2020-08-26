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
            rows = self.lst[index].find_all('tr')
            res = []
            for tr in rows:
                th = tr.find_all('th')
                if th:
                    keys.append([tr.text.strip() for tr in th if tr.text.strip()])

                td = tr.find_all('td')
                row = [tr.text.strip() for tr in td if tr.text.strip()]
               
                if row:
                    res.append(row)
            print("Keys :",keys,"\nValues : ",res)

        elif order == "column":
            columns = self.lst[index].find_all('tr')
            print(columns)
            
        else:
            return "Invalid Arguments"
        return "Hola"