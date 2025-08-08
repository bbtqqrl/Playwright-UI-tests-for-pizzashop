from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def login_in_account(self, username, password):
        self.page.locator("input[name='username']").fill(username)
        self.page.locator("input[name='password']").fill(password)
        self.page.locator("button[type='submit']:has-text('Log in')").click()
    
