import pytest
import asyncio
from playwright.sync_api import Page, expect, sync_playwright

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         # For debugging, set headless=False
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         yield browser
#         browser.close()

# @pytest.fixture(scope="function")
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()

# def test_add_pizza_to_cart(page: Page):
#     # Відкрити сайт
#     page.goto("https://pizza-if.com/")

#     # Клік на "Піца"
#     page.locator("a:has-text('Піца')").first.click()


#     # Додати "П’ять сирів" у кошик
#     page.get_by_role("link", name="Add “П’ять сирів” to your cart").click()

#     # Клік на "Замовити"
#     page.get_by_role("link", name="Замовити").click()
#     page.get_by_role("button", name="Оформити замовлення").click()
#     page.get_by_role("button", name="Оформити замовлення").click()

#     # Перевіряємо, що на сторінці є повідомлення про помилку
#     expect(page.locator("body")).to_contain_text("Не всі дані вказані")

from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.pizza_page import PizzaPage
from pages.cart_page import CartPage

def test_add_pizza_to_cart_without_all_data(page: Page):
    page.goto("https://pizza-if.com")
    home_page = HomePage(page)
    pizza_page = PizzaPage(page)
    cart_page = CartPage(page)

    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    cart_page.submit_order()
    cart_page.submit_order()
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")