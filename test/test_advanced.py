from playwright.sync_api import sync_playwright

def dimentions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=5000)
        context = browser.new_context(viewport={'width':500,'height':400})
        page = context.new_page()
        page.goto('https://www.amazon.in/')


def MobileDevice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=5000)
        context = browser.new_context(**p.devices["iPhone XR"])
        page = context.new_page()
        page.goto('https://www.amazon.in/')


def geoLocation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=5000)
        context = browser.new_context(geolocation={'latitude':37.269175 ,'longitude':-119.30661},permissions=["geolocation"])
        page = context.new_page()
        page.goto('https://browserleaks.com/geo')




def test_networkMock():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=5000)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        context.set_offline(True)
        page.get_by_text('Online Trainings').click()
        context.set_offline(False)
        page.reload()

