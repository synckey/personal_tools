#!/usr/bin/env python
# -*-coding:utf-8-*-
import json
import sys
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

def process_phonetic(line):
    result = ""
    try:
        result = line.get("cell")[2].split("<us>")[1]
    except Exception, e:
        pass
    if result:
        result = result.replace("</us>", "")
    return result


def process_chinese(word):
    meaning = word.get("cell")[3]

    if meaning:
        meaning = meaning.replace("名 词", "\n名词").replace("副 词", "\n副词").replace("时 态", "\n时态").replace("1. ", ""). \
            replace("2. ", "\n").replace("3. ", "\n").replace("4. ", "\n").replace(",", "，").replace("  ", " ")
        meaning = meaning.replace("<br>", " ")
    return "\"" + meaning + "\""

#"http://dict.eudic.net/StudyList/GridData?catid=1462587646&_search=false&nd=1463538467821&rows=100000&page=1&sidx=&sord=asc")
content = ""
with open("GridData.json") as f:
    for line in f:
        content += line
content = json.loads(content)
result = ""
for row in content.get("rows"):
    result += row.get("id") + "," + process_phonetic(row).replace(",", "ˌ") + "," + process_chinese(row) + "\r\n"
with open("words.csv", "w") as f:
    f.write(result)
