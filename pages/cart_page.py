from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def submit_order(self):
        self.page.get_by_text("Оформити замовлення").click()
    
    def input_data_order(self, name, phone, email, address, comment):
        self.page.locator("input[name='name']").fill(name)
        self.page.locator("input[name='phone']").fill(phone)
        self.page.locator("input[name='email'][placeholder='Email (не обов’язково)']").fill(email)
        self.page.locator("input[name='address']").fill(address)
        self.page.locator("textarea[name='comment']").fill(comment)
    
    def get_summ(self):
        total = self.page.locator("#checkount_total").inner_text()
        return total

    