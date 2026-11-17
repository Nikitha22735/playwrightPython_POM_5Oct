import json

from playwright.sync_api import Page, expect

from pages.auth import Auth
from pages.home import HomePage
from utils.jsonHandling import grabJsonValue


def test_validatePositiveLogin(page: Page,amazonNavigation):
    HomePageObj = HomePage(page)
    authObj = Auth(page)
    HomePageObj.clickOnAccountNdList()   
    creds = grabJsonValue('utils/jsonHandling.py')
    # authObj.enterEmail("trainingplaywright@gmail.com")   
    authObj.enterEmail(creds["login"])   
    authObj.clickOnContinueBtn()
    authObj.fillPw("Welcome@04")
    authObj.signInBtn()
    HomePageObj.validateTheVisibilityOfSearchBox()




def test_validateNegitiveLogin(page: Page,amazonNavigation):
    HomePageObj = HomePage(page)
    authObj = Auth(page)
    HomePageObj.clickOnAccountNdList()  
    authObj.enterEmail("trainingplaywright@gmail.com")
    authObj.clickOnContinueBtn()
    authObj.fillPw("yyyyy@04")
    authObj.signInBtn()
    authObj.validateIncorrectPwMsg()

