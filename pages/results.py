from playwright.sync_api import Page, expect


class ResultsPage:
    def __init__(self, page: Page):
        self.resultsHeading = page.get_by_role("heading", name="Results", exact=True)
        self.addToCartButton = page.locator("#a-autoid-3").get_by_role(
            "button", name="Add to cart"
        )

    def validateResultsPageVisible(self):
        expect(self.resultsHeading).to_be_visible()

    def addFirstResultToCart(self):
        self.addToCartButton.click()