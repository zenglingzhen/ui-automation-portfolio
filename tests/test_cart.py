
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from test_data import (
    STANDARD_USER,
    PASSWORD,
    BACKPACK,
    BIKE_LIGHT,
    BACKPACK_NAME,
    BIKE_LIGHT_NAME,
)

def test_add_product_to_cart(app_page):
    # 1. 登录
    login_page = LoginPage(app_page)
    login_page.login(STANDARD_USER, PASSWORD)

    products_page = ProductsPage(app_page)
    products_page.add_product_to_cart(BACKPACK)

    # 添加第二件商品
    products_page.add_product_to_cart(BIKE_LIGHT)

    # 打开购物车
    cart_page = CartPage(app_page)
    cart_page.open_cart()

    # 验证购物车商品数量和名称
    cart_page.verify_cart_item_count(2)
    # 验证两件商品名称
    expect(cart_page.product_names).to_contain_text([
        BACKPACK_NAME,
        BIKE_LIGHT_NAME
    ])

    def test_remove_product_from_cart(app_page):
        # 1. 登录
        login_page = LoginPage(app_page)
        login_page.login(STANDARD_USER, PASSWORD)

        # 2. 添加商品，为删除操作准备测试数据
        products_page = ProductsPage(app_page)
        products_page.add_product_to_cart(BACKPACK)

        # 3. 打开购物车
        cart_page = CartPage(app_page)
        cart_page.open_cart()

        # 4. 确认删除前有一件商品
        cart_page.verify_cart_item_count(1)

        # 5. 删除商品
        cart_page.remove_product(BACKPACK)

        # 6. 验证删除结果
        cart_page.verify_cart_item_count(0)
        expect(app_page.locator(".shopping_cart_badge")).to_have_count(0)


