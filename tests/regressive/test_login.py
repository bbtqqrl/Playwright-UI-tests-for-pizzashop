from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import json
import pytest

@pytest.mark.parametrize("username, password", [
    # Звичайні негативні тести
    ("", "valid_password"), 
    ("valid_user", ""),   
    ("¼", "123456"),        
    ("legit", "¼"),          
    
    # XSS-атаки
    ("<script>alert('XSS')</script>", "password123"),
    ("admin", "<img src=x onerror=alert(1)>"),
    
    # SQL-ін'єкції
    ("admin'--", "any_password"),
    ("' OR '1'='1", "' OR '1'='1"),
    
    # Інші невалідні дані
    ("A" * 256, "password"),
    ("admin", "A" * 256),      
])
def test_negative_login(page: Page, username, password):
    page.goto("https://pizza-if.com/my-account/")
    login_page = LoginPage(page)
    login_page.login_in_account(username, password)
    
    error_message = page.locator('ul.woocommerce-error[role="alert"]')
    expect(error_message).to_be_visible()
