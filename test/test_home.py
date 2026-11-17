import re
from playwright.sync_api import Page, expect
from pages.home import HomePage

def test_validate_the_UI_for_home_screen(page: Page, amazonNavigation):
    HomePageObj = HomePage(page)
    HomePageObj.validateTheVisibilityOfAmazonLogo()
    HomePageObj.validateTheVisibilityOfSearchBox()
    HomePageObj.validateTheVisibilityOfAddToCart()



def test_validate_the_EN_flag(page: Page, amazonNavigation):
    HomePageObj = HomePage(page)
    HomePageObj.validateTheVisibilityOfFlag()
    
    

