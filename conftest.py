
import pytest


@pytest.fixture()
def amazonNavigation(page):
    page.goto("https://www.amazon.in/")