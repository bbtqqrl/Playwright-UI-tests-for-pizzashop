from playwright.sync_api import Page, expect
import pytest

def test_sorting_pizzas(page, home_page, goods_page):
    home_page.open_pizza_menu()
    goods_page.sort_pizzas("Sort by price: low to high")
    sort_prices = goods_page.get_pizzas_prices()
    assert sort_prices == sorted(sort_prices)

