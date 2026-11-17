import json

from playwright.sync_api import Page, expect

def test_jsonHandling():
    with open('testData/creds.json') as data:
        creds = json.load(data)
        print(creds["login"])