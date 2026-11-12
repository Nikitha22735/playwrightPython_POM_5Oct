import re
from playwright.sync_api import Page, expect


def test_validate_the_UI_for_home_screen(page: Page):
    page.goto("https://www.amazon.in/")
    expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
    expect(page.get_by_role("link", name="items in cart")).to_be_visible()



def test_validate_the_EN_flag(page: Page):
    page.goto("https://www.amazon.in/")
    expect(page.locator("//div[text()='EN']")).to_be_visible()
    

