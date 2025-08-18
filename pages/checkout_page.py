from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CheckoutPage(BasePage):
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
        return int(''.join(filter(str.isdigit, total)))

    def delete_from_checkout(self, name: str):
        self.page.get_by_role("link", name=f"Remove {name} from cart").click()

    def delete_first_from_checkout(self):
        first_name = self.page.locator("div.cart-product__title").first.text_content()
        first_name = first_name.rsplit(" ", 1)[0]
        self.page.get_by_role("link", name=f"Remove {first_name} from cart").click()

    def get_item_price(self, name: str):
        price_text = self.page.locator(f"div.checkount__cart:has(div.cart-product__title:has-text('{name}')) span.price-cart-item").inner_text()
        return int(''.join(filter(str.isdigit, price_text)))
    

