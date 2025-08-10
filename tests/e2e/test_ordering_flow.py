from playwright.sync_api import Page, expect
import pytest
from pages.home_page import HomePage
from pages.pizza_page import PizzaPage
from pages.cart_page import CartPage
@pytest.mark.skip(reason="Skipping test for ordering pizza without phone")

def test_ordering_pizza_without_all_data(page: Page):
    page.goto("https://pizza-if.com")
    home_page = HomePage(page)
    pizza_page = PizzaPage(page)
    cart_page = CartPage(page)

    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    cart_page.submit_order()
    cart_page.submit_order()
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")

@pytest.mark.skip(reason="Skipping test for ordering pizza without phone")
def test_ordering_pizza_withot_phone(page: Page):
    page.goto("https://pizza-if.com")
    home_page = HomePage(page)
    pizza_page = PizzaPage(page)
    cart_page = CartPage(page)

    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    cart_page.input_data_order('Max', '090', '090', 'Kyiv', 'Test comment')
    cart_page.submit_order()
    validation_msg = page.locator("input[name='email'][placeholder='Email (не обов’язково)']").evaluate("el => el.validationMessage")
    assert validation_msg != ''


# @pytest.mark.xfail(reason="bug: Test for ordering pizza without pizza is not implemented yet")
def test_ordering_pizza_without_pizza(page, home_page, pizza_page, cart_page):
    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    pizza_page.delete_pizza_from_cart(pizza_name="Піца Бомбей")
    cart_page.input_data_order('Max', '090', '', 'Kyiv', 'Test comment')
    cart_page.submit_order()
    cart_page.submit_order()
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")