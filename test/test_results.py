import re
from playwright.sync_api import Page, expect


def test_validateResultsUI(page: Page, amazonNavigation):
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone")
    page.get_by_role("button", name="Go", exact=True).click()
    expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
    expect(page.get_by_text("Eligible for Free Delivery")).to_be_visible()
