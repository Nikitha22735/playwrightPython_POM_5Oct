import csv
import json
import os
from openpyxl import load_workbook
import pytest
from dotenv import load_dotenv
# from openpyxl import load_workbook 

from playwright.sync_api import Page, expect

def test_jsonHandling():
    with open('testData/creds.json') as data:
        creds = json.load(data)
        print(creds["login"])


def test_csvHandling():
    with open('testData\\credentails.csv') as data:
        data1 = csv.DictReader(data)
        l1 = []
        for i in data1:
            l1.append(i)
        print(l1)

def test_excel():
    workbook = load_workbook("testData\\sample_creds.xlsx")
    sheetdata = workbook["Sheet3"]
    l1 = []
    for i in sheetdata.iter_rows(min_row=2,values_only=True):
        l1.append(i)
    print(l1)



def test_excel_write():
    workbook = load_workbook("testData\\sample_creds.xlsx")
    sheetdata = workbook["Sheet3"]
    sheetdata["A3"]="testing"
    sheetdata.append(["tst1",'tst2'])
    sheetdata.delete_rows(3,1)
    workbook.save("testData\\sample_creds.xlsx")

# set cred1_usname=testing1&&set cred1_pw=pw&&pytest -m dh -s

def test_cl1():
    print(os.getenv("cred1_usname"))
    print(os.getenv("cred1_pw"))

#pip install pytest-dotenv
@pytest.mark.dh
def test_dotenv():
    load_dotenv(os.getenv('data'))
    print(os.getenv("usname1"))
    print(os.getenv("pw1"))
 





