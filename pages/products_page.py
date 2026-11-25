
from playwright.sync_api import Page,expect

class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        # 商品页面元素
        self.product_list = page.locator(".inventory_list")
        self.products = page.locator(".inventory_item")

    # 获取商品数量
    def get_product_count(self):
        return self.products.count()

    # 检查商品列表是否显示
    def verify_product_list_visible(self):
        expect(self.product_list).to_be_visible()
    #商品添加
    def add_product_to_cart(self, product_id):
        self.page.locator(
            f'[data-test="add-to-cart-{product_id}"]'
        ).click()

