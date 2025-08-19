from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class ConstructorPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def add_stuf(self, goods_name: str):
        self. page.locator('button[data-type="plus"][class="extra-btn-konstruktor"]').first.click()
    
