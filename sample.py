import requests

url = 'https://127.0.0.1:8000/'

x = requests.get(url)

print(x.status_code)