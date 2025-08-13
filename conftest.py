import sys
import os
import pytest
from playwright.sync_api import sync_playwright, Page
from pages.home_page import HomePage
from pages.pizza_page import PizzaPage
from pages.checkout_page import CheckoutPage
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture
def page(page: Page):  # playwright фікстура
    page.goto("https://pizza-if.com")
    yield page
    # Тут можна додати cleanup (наприклад, очистку cookies)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def pizza_page(page: Page) -> PizzaPage:
    return PizzaPage(page)

@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)
