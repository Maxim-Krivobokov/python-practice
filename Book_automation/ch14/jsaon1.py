import json

StringOfJsonData = '{"name": "Zophie", "isCat": true, "micecaught": 0, "felineIQ": null}'


print(type(StringOfJsonData))

jsonDataAsPythonValue = json.loads(StringOfJsonData)


print(type(jsonDataAsPythonValue))