
# import allure
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

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     result = outcome.get_result()

#     if result.failed:
#         page = item.funcargs.get("page")
#         if page:
#             allure.attach(
#                 page.screenshot(),
#                 name="failedstep",
#                 attachment_type=allure.attachment_type.PNG
#             )
