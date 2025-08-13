from playwright.sync_api import Page, expect
import pytest

def test_ordering_pizza_without_all_data(page, home_page, pizza_page, checkout_page):
    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    checkout_page.submit_order()
    checkout_page.submit_order()
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")

def test_ordering_pizza_withot_phone(page, home_page, pizza_page, checkout_page):
    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    checkout_page.input_data_order('Max', '090', '090', 'Kyiv', 'Test comment')
    checkout_page.submit_order()
    validation_msg = page.locator("input[name='email'][placeholder='Email (не обов’язково)']").evaluate("el => el.validationMessage")
    assert validation_msg != ''


@pytest.mark.skip(reason="bug: Test for ordering pizza without pizza is not implemented yet")
def test_ordering_without_items(page, home_page, pizza_page, checkout_page):
    home_page.open_pizza_menu()
    pizza_page.order_pizza("Піца Бомбей")
    checkout_page.delete_from_checkout("Піца Бомбей")
    checkout_page.input_data_order('Max', '0951127692', '', 'Kyiv', 'Test comment')
    checkout_page.submit_order()
    checkout_page.submit_order()
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")