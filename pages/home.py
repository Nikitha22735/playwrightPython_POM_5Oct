
from playwright.sync_api import Page, expect

from utils.allure_steps import test_step


class HomePage:
    def __init__(self,page):
        self.accountsNdList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchBoxTextbox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.amazonLogo = page.get_by_role("link", name="Amazon.in")
        self.cartIcon = page.get_by_role("link", name="items in cart")
        self.flag = page.locator("//div[text()='EN']")


    def clickOnAccountNdList(self):
        with test_step("clickOnAccountNdList"):
            self.accountsNdList.click()

    def validateTheVisibilityOfSearchBox(self):
        with test_step("validateTheVisibilityOfSearchBox"):
            expect(self.searchBoxTextbox).to_be_visible()

    def validateTheVisibilityOfAmazonLogo(self):
        with test_step("validateTheVisibilityOfAmazonLogo"):
            expect(self.amazonLogo).to_be_visible()

    def validateTheVisibilityOfAddToCart(self):
        with test_step("validateTheVisibilityOfAddToCart"):
            expect(self.cartIcon).not_to_be_visible()
        
    def validateTheVisibilityOfFlag(self):
        with test_step("validateTheVisibilityOfFlag"):
            expect(self.flag).to_be_visible()