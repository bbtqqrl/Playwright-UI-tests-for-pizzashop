import sys
import os
import pytest
from playwright.sync_api import sync_playwright, Page
from pages.home_page import HomePage
from pages.goods_page import GoodsPage
from pages.checkout_page import CheckoutPage
import time
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
def goods_page(page: Page) -> GoodsPage:
    return GoodsPage(page)

@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)

@pytest.fixture
def cart_with_pizza(home_page, goods_page):
    home_page.open_pizza_menu()
    goods_page.order_pizza("Піца Бомбей")

@pytest.fixture
def cart_with_sushi(home_page, sushi_page):
    home_page.open_sushi_menu()
    goods_page.order_sushi("Червоний дракон")

@pytest.fixture
def test_user():
    return{"name": "Max",
    "phone": "0957777777", 
    "email": f"test_{int(time.time())}@test.com",
    "address": "Kyiv",
    "comment": "Test comment"}
