from libs.lib_fetch import Fetcher

obj = Fetcher('https://www.w3schools.com/html/html_tables.asp')
print(obj.extract())