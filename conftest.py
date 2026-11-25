
import allure
from pages.auth import Auth
from pages.home import HomePage
import pytest
from utils.jsonHandling import grabJsonValue
from playwright.sync_api import Page, expect, sync_playwright


@pytest.fixture()
def amazonNavigation(page):
    page.goto("https://www.amazon.in/")

@pytest.fixture()
def login(page,amazonNavigation):
    HomePageObj = HomePage(page)
    authObj = Auth(page)
    HomePageObj.clickOnAccountNdList()   
    creds = grabJsonValue('utils/jsonHandling.py')
    # authObj.enterEmail("trainingplaywright@gmail.com")   
    authObj.enterEmail(creds["login"])   
    authObj.clickOnContinueBtn()
    authObj.fillPw("Welcome@04")
    authObj.signInBtn()
    HomePageObj.validateTheVisibilityOfSearchBox()
    # yield
    # logout

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.failed and result.when == "call":
        pages = []
        for value in item.funcargs.values():
            if callable(getattr(value, "screenshot", None)):
                pages.append(value)
            else:
                pages.extend(
                    page for page in getattr(value, "pages", [])
                    if callable(getattr(page, "screenshot", None))
                )

        for index, page in enumerate(pages, start=1):
            allure.attach(
                page.screenshot(),
                name=f"failedstep-{index}",
                attachment_type=allure.attachment_type.PNG
            )






# @pytest.fixture(scope="session")
# def cookies():
#      with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False,slow_mo=5000)
#             context = browser.new_context()
#             page = context.new_page()
#             page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#             page.get_by_role("textbox", name="Username").click()
#             page.get_by_role("textbox", name="Username").fill("Admin")
#             page.get_by_role("textbox", name="Password").click()
#             page.get_by_role("textbox", name="Password").fill("admin123")
#             page.get_by_role("button", name="Login").click()
#             expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
#             context.storage_state(path='testData\\cookies.json')


# @pytest.fixture()
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False,slow_mo=5000)
#         context = browser.new_context(storage_state='testData\\cookies.json')
#         page = context.new_page()
#         yield page