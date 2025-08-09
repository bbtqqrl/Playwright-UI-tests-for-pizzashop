from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import json
import pytest

@pytest.mark.parametrize("username, password", [
    # Звичайні негативні тести
    ("", "valid_password"),  # Пустий логін
    ("valid_user", ""),      # Пустий пароль
    ("¼", "123456"),         # Спецсимволи
    ("legit", "¼"),          # Спецсимволи
    
    # XSS-атаки
    ("<script>alert('XSS')</script>", "password123"),
    ("admin", "<img src=x onerror=alert(1)>"),
    
    # SQL-ін'єкції
    ("admin'--", "any_password"),
    ("' OR '1'='1", "' OR '1'='1"),
    
    # Інші невалідні дані
    ("A" * 256, "password"),  # Дуже довгий логін
    ("admin", "A" * 256),      # Дуже довгий пароль
])
def test_negative_login(page: Page, username, password):
    page.goto("https://pizza-if.com/my-account/")
    login_page = LoginPage(page)
    login_page.login_in_account(username, password)
    
    error_message = page.locator('ul.woocommerce-error[role="alert"]')
    expect(error_message).to_be_visible()
    
    console_errors = []
    for msg in page.context.logs:
        if msg.level == "error":
            console_errors.append(msg.text)
    assert not console_errors, f"Є помилки в консолі: {console_errors}"