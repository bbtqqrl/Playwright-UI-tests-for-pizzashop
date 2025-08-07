from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def click(self, locator: str):
        self.page.locator(locator).click()
    
    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
    
    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
    
    def wait_for_selector(self, locator: str):
        self.page.locator(locator).wait_for()
    
    def should_be_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()