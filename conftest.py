
import allure
import pytest


@pytest.fixture()
def amazonNavigation(page):
    page.goto("https://www.amazon.in/")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="failedstep",
                attachment_type=allure.attachment_type.PNG
            )
