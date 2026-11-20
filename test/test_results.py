import re
from playwright.sync_api import Page, expect
from pages.home import HomePage

# from utils.allure_steps import test_step


def test_validateResultsUI(page: Page, amazonNavigation):
        HomePage(page).searchFor("iphone")
        expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
        expect(page.get_by_text("Eligible for Free Delivery")).to_be_visible()
