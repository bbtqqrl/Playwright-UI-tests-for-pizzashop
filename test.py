import pytest
import asyncio
from playwright.sync_api import Page, expect, sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # For debugging, set headless=False
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_add_pizza_to_cart(page: Page):
    # Відкрити сайт
    page.goto("https://pizza-if.com/")

    # Клік на "Піца"
    page.locator("a:has-text('Піца')").first.click()


    # Додати "П’ять сирів" у кошик
    page.get_by_role("link", name="Add “П’ять сирів” to your cart").click()

    # Клік на "Замовити"
    page.get_by_role("link", name="Замовити").click()
    page.get_by_role("button", name="Оформити замовлення").click()
    page.get_by_role("button", name="Оформити замовлення").click()

    # Перевіряємо, що на сторінці є повідомлення про помилку
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")