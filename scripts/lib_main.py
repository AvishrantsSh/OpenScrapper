from libs.lib_fetch import Fetcher
# Alpha Stage
obj = Fetcher('http://127.0.0.1:8000/tmp/')
array = obj.extract()
print(obj.jsonify(0), "row")