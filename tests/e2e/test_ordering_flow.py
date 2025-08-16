from playwright.sync_api import Page, expect



def test_phone_validation(test_user, cart_with_pizza, page, checkout_page):
    test_user["phone"] = "" 
    checkout_page.input_data_order(
        **test_user
    )
    checkout_page.submit_order()
    checkout_page.submit_order()
    expect(page.locator("body")).to_contain_text("Не всі дані вказані")

def test_mail_validation(test_user, cart_with_pizza, page,  checkout_page):
    test_user["email"] = "invalid_email" 
    checkout_page.input_data_order(
        **test_user
    )
    checkout_page.submit_order()
    checkout_page.submit_order()
    validation_msg = page.locator("input[name='email'][placeholder='Email (не обов’язково)']").evaluate("el => el.validationMessage")
    assert validation_msg != ''

def test_successful_order(test_user, cart_with_pizza, page, checkout_page):
    checkout_page.input_data_order(
        **test_user
    )
    checkout_page.submit_order()
    expect(page.locator("body")).to_contain_text("Замовлення оформлено")
