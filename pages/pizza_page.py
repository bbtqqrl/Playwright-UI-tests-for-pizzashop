from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class PizzaPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def select_pizza(self, pizza_name: str):
        self.page.locator(f"div.product-item__title:has-text('{pizza_name}')").click()
    
    def add_pizza_to_cart(self, pizza_name: str):
        self.page.get_by_role("link", name=f"Add “{pizza_name}” to your cart").click()
        self.page.locator("button.modal-close:has-text('Продовжити покупки')").click()
    
    def order_pizza(self, pizza_name: str):
        self.page.get_by_role("link", name=f"Add “{pizza_name}” to your cart").click()
        self.page.get_by_role("link", name="Замовити").click()
    