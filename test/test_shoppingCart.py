from playwright.sync_api import Page

from pages.home import HomePage
from pages.results import ResultsPage
from pages.shoppingCarts import ShoppingCartPage


def test_add_iphone_to_cart(page: Page, amazonNavigation):
    homePage = HomePage(page)
    homePage.searchFor("iphone")

    resultsPage = ResultsPage(page)
    resultsPage.addFirstResultToCart()

    shoppingCartPage = ShoppingCartPage(page)
    shoppingCartPage.openCart()
    shoppingCartPage.validateShoppingCartIsVisible()


def test_cart_count_increases_after_adding_iphone(page: Page):
    page.goto("https://www.google.com/")
    page.goto("https://www.amazon.in/")

    homePage = HomePage(page)
    homePage.searchFor("iphone")

    resultsPage = ResultsPage(page)
    resultsPage.validateResultsPageVisible()
    cartCountBeforeAdd = homePage.getCartCount()

    resultsPage.addFirstResultToCart()
    homePage.validateCartCountIncreasedByOne(cartCountBeforeAdd)