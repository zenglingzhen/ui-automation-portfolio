
from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        # 用户信息输入框
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')

        # 继续按钮
        self.continue_button = page.locator('[data-test="continue"]')

        # 订单概览页标题
        self.overview_title = page.locator(".title")

        # 订单商品
        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")

        # 订单金额
        self.subtotal = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")

        # Finish 按钮
        self.finish_button = page.locator('[data-test="finish"]')

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def verify_overview_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-two.html"
        )
        expect(self.overview_title).to_have_text("Checkout: Overview")

    def verify_order_item_count(self, count):
        expect(self.cart_items).to_have_count(count)

    def verify_product_name(self, name):
        expect(self.product_names).to_have_text(name)

    def get_subtotal(self):
        return self.subtotal.inner_text()

    def get_total(self):
        return self.total.inner_text()

    def finish_checkout(self):
        self.finish_button.click()

    def verify_checkout_complete(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-complete.html"
        )

        complete_title = self.page.locator(".complete-header")
        expect(complete_title).to_have_text("Thank you for your order!")

        complete_message = self.page.locator(".complete-text")
        expect(complete_message).to_contain_text(
            "Your order has been dispatched"
        )
