from libs.lib_fetch import Fetcher
# Alpha Stage
obj = Fetcher('https://www.w3schools.com/html/html_tables.asp')
print(obj.extract())