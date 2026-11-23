
import allure
from pages.auth import Auth
from pages.home import HomePage
import pytest
from utils.jsonHandling import grabJsonValue


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
