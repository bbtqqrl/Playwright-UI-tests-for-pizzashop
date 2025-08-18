from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
