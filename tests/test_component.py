from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import json

def test_negative_login(page: Page):
    page.goto("https://pizza-if.com/my-account/")
    login_page = LoginPage(page)
    login_page.login_in_account("invalid_user", "invalid_password")
    
    error_message = page.locator(".error-message").text_content()
    assert "Неправильний логін або пароль" in error_message
