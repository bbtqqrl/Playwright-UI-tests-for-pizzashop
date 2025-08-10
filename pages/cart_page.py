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

    def delete_pizza_from_cart(self, pizza_name: str):
        self.page.get_by_role("link", name=f"Remove {pizza_name} from cart").click()

    def delete_first_pizza_from_cart(self):
        first_pizza_name = self.page.locator("div.cart-product__title").first.text_content()
        first_pizza_name = first_pizza_name.rsplit(" ", 1)[0]
        self.page.get_by_role("link", name=f"Remove {first_pizza_name} from cart").click()
    
    def add_pizza_to_cart(self, pizza_name: str):
        self.page.get_by_role("link", name=f"Add “{pizza_name}” to your cart").click()
        self.page.locator("button.modal-close:has-text('Продовжити покупки')").click()
    