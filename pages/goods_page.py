from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class GoodsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def select_goods(self, goods_name: str):
        self.page.locator(f"div.product-item__title:has-text('{goods_name}')").click()
    
    def order_goods(self, goods_name: str):
        self.page.get_by_role("link", name=f"Add “{goods_name}” to your cart").click()
        self.page.get_by_role("link", name="Замовити").click()

    def add_food_to_cart(self, name: str):
        self.page.get_by_role("link", name=f"Add “{name}” to your cart").click()
        self.page.locator("button.modal-close:has-text('Продовжити покупки')").click()
    
    def sort_goods(self, sort_by: str):
        self.page.locator(f"select.orderby").select_option(sort_by)
    
    def get_goods_prices(self) -> str:
        self.page.wait_for_selector("div.product-item__price")  
        prices = self.page.locator("div.product-item__price").all_inner_texts()
        prices = [int(''.join(filter(str.isdigit, price))) for price in prices]
        return prices