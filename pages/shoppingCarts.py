from playwright.sync_api import Page, expect


class ShoppingCartPage:
    def __init__(self, page: Page):
        self.cartLink = page.get_by_role("link", name="item in cart")
        self.shoppingCartHeading = page.get_by_role(
            "heading", name="Shopping Cart"
        )

    def openCart(self):
        self.cartLink.click()

    def validateShoppingCartIsVisible(self):
        expect(self.shoppingCartHeading).to_be_visible()