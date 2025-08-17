from pages.base_page import BasePage
from pages.goods_page import GoodsPage
from playwright.sync_api import Page, expect

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_pizza_menu(self):
        self.page.locator("a:has-text('Піца')").first.click()
        return GoodsPage(self.page)

    def open_sushi_menu(self):
        self.page.locator("a:has-text('Суші')").first.click()
    
    # def open_cart(self):
    #     self.click(self.)
    
    # def open_login_form(self):
    #     self.click(self.login_button)