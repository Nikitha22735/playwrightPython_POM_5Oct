import json


def grabJsonValue(filePath):
     with open(filePath) as data:
            creds = json.load(data) 
            return creds