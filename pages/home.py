
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self,page):
        self.accountsNdList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchBoxTextbox = page.get_by_role("searchbox", name="Search Amazon.in")


    def clickOnAccountNdList(self):
          self.accountsNdList.click()


    def validateTheVisibilityOfSearchBox(self):
         expect(self.searchBoxTextbox).to_be_visible()