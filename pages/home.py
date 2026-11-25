
from playwright.sync_api import Page, expect

# from utils.allure_steps import test_step


class HomePage:
    def __init__(self, page):
        self.accountsNdList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchBoxTextbox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.searchButton = page.get_by_role("button", name="Go", exact=True)
        self.amazonLogo = page.get_by_role("link", name="Amazon.in")
        self.cartIcon = page.get_by_role("link", name="items in cart")
        self.cartCount = page.locator("#nav-cart-count")
        self.flag = page.locator("//div[text()='EN']")


    def clickOnAccountNdList(self):
            self.accountsNdList.click()

    def validateTheVisibilityOfSearchBox(self):
            expect(self.searchBoxTextbox).to_be_visible()

    def searchFor(self, productName: str):
            self.searchBoxTextbox.fill(productName)
            self.searchButton.click()

    def getCartCount(self) -> int:
            expect(self.cartCount).to_be_visible()
            return int(self.cartCount.inner_text().strip())

    def validateCartCountIncreasedByOne(self, previousCount: int):
            expect(self.cartCount).to_have_text(str(previousCount + 1))

    def validateTheVisibilityOfAmazonLogo(self):
            expect(self.amazonLogo).to_be_visible()

    def validateTheVisibilityOfAddToCart(self):
            expect(self.cartIcon).not_to_be_visible()
        
    def validateTheVisibilityOfFlag(self):
            expect(self.flag).to_be_visible()