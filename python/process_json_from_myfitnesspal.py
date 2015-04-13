from datetime import date

__author__ = 'wangjian03'
"""
   process the data from http://www.myfitnesspal.com/reports/results/progress/1/365.json?report_name=Weight
"""
import json

jsonstring = ""
JSON_FILE = "365.json"

with open(JSON_FILE) as f:
    for line in f:
        jsonstring = jsonstring + line.strip()
data = json.loads(jsonstring)
result = []
tmp = 0
count = 0
for point in data["data"]:
    if point["total"] > 0:
        if tmp == point["total"]:
            count += 1
            if count > 2:
                continue
        else:
            count = 0
            tmp = point["total"]

        month = int(point["date"].split("/")[0])
        day = int(point["date"].split("/")[1])
        year = 2015
        if month in [11, 12]:
            year = 2014
        time_line = date(year, month, day)
        result.append({"date":time_line.strftime("%Y-%m-%d"),"total":point["total"]})
print json.dumps(result)
key=[]
value=[]
for point in result:
    key.append(point.get("date"))
    value.append(point.get("total"))
print json.dumps(key)
print json.dumps(value)
