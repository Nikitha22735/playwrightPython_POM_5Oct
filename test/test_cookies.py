
from playwright.sync_api import Page, expect, sync_playwright


def cookies():
     with sync_playwright() as p:
            browser = p.chromium.launch(headless=False,slow_mo=5000)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            page.get_by_role("textbox", name="Username").click()
            page.get_by_role("textbox", name="Username").fill("Admin")
            page.get_by_role("textbox", name="Password").click()
            page.get_by_role("textbox", name="Password").fill("admin123")
            page.get_by_role("button", name="Login").click()
            expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
            context.storage_state(path='testData\\cookies.json')


def test_tc1():
       with sync_playwright() as p:
                  browser = p.chromium.launch(headless=False,slow_mo=5000)
                  context = browser.new_context(storage_state="testData\\cookies.json")
                  page = context.new_page()
                  page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
      
