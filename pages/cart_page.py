
from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # 购物车页面元素
        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(".inventory_item_name")

    # 验证购物车商品数量
    def verify_cart_item_count(self, count):
        expect(self.cart_items).to_have_count(count)

    # 验证商品名称
    def verify_product_name(self, name):
        expect(self.product_names).to_have_text(name)

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def remove_product(self, product_id):
        self.page.locator(
            f'[data-test="remove-{product_id}"]'
        ).click()

    def click_checkout(self):
        self.page.locator('[data-test="checkout"]').click()