from playwright.sync_api import Page, expect
import pytest

# # Happy path tests
# def test_ordering_pizza(page, home_page, pizza_page, checkout_page):
#     home_page.open_pizza_menu()
#     pizza_page.order_pizza("Піца Бомбей")
#     checkout_page.input_data_order('Max', '0957777777', '', 'Kyiv', 'Test comment')
#     checkout_page.submit_order()
#     validation_msg = page.locator("input[name='email'][placeholder='Email (не обов’язково)']").evaluate("el => el.validationMessage")
#     assert validation_msg != ''

# # Negative tests
# def test_ordering_pizza_without_all_data(page, home_page, pizza_page, checkout_page):
#     home_page.open_pizza_menu()
#     pizza_page.order_pizza("Піца Бомбей")
#     checkout_page.submit_order()
#     checkout_page.submit_order()
#     expect(page.locator("body")).to_contain_text("Не всі дані вказані")

def test_ordering_pizza_withot_phone(page, home_page, pizza_page, checkout_page):
    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    checkout_page.input_data_order('Max', '', '', 'Kyiv', 'Test comment')
    checkout_page.submit_order()
    validation_msg = page.locator("input[name='email'][placeholder='Email (не обов’язково)']").evaluate("el => el.validationMessage")
    assert validation_msg != ''

# @pytest.mark.xfail(reason="bug: Test for ordering pizza without pizza is not implemented yet")
# def test_ordering_without_items(page, home_page, pizza_page, checkout_page):
#     home_page.open_pizza_menu()
#     pizza_page.order_pizza("Піца Бомбей")
#     checkout_page.delete_from_checkout("Піца Бомбей")
#     checkout_page.input_data_order('test', '095', '', 'test', 'Test comment')
#     checkout_page.submit_order()
#     checkout_page.submit_order()
#     # expect(page.locator("body")).to_contain_text("Не всі дані вказані")

import pytest
from playwright.sync_api import Page, expect

# Фікстура для підготовки кошика з піцою

# Тест на валідацію телефону
def test_phone_validation(cart_with_pizza, checkout_page):
    checkout_page.input_data_order(name='Max', phone='', email='', address='Kyiv')
    checkout_page.submit_order()
    checkout_page.submit_order()
    expect(checkout_page.locator("body")).to_contain_text("Не всі дані вказані")

# Тест на пустий кошик
def test_empty_cart_error(checkout_page):
    checkout_page.open()
    checkout_page.submit_order()
    expect(checkout_page.global_error).to_contain_text("Додайте піцу")

# Тест на успішне замовлення (happy path)
def test_successful_order(cart_with_pizza, checkout_page):
    checkout_page.input_data_order(name='Max', phone='0957777777', email='test@test.com', address='Kyiv')
    checkout_page.submit_order()
    expect(checkout_page.success_message).to_be_visible()