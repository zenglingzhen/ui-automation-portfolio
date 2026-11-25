from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data import (
    STANDARD_USER,
    PASSWORD,
    BACKPACK,
    BACKPACK_NAME,
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    BACKPACK_PRICE,
    BACKPACK_TOTAL,
)


def test_checkout_with_customer_info(app_page):
    # 1. 登录
    login_page = LoginPage(app_page)
    login_page.login(STANDARD_USER, PASSWORD)

    # 2. 添加商品
    products_page = ProductsPage(app_page)
    products_page.add_product_to_cart(BACKPACK)

    # 3. 打开购物车
    cart_page = CartPage(app_page)
    cart_page.open_cart()

    # 4. 验证购物车有一件商品
    cart_page.verify_cart_item_count(1)

    # 5. 点击 Checkout
    cart_page.click_checkout()

    # 6. 填写用户信息
    checkout_page = CheckoutPage(app_page)
    checkout_page.fill_customer_info(
        FIRST_NAME,
        LAST_NAME,
        POSTAL_CODE
    )

    # 7. 点击 Continue
    checkout_page.continue_checkout()

    # 8. 验证进入订单概览页
    checkout_page.verify_overview_page()

    # 9. 验证订单商品数量
    checkout_page.verify_order_item_count(1)

    # 10. 验证商品名称
    checkout_page.verify_product_name(BACKPACK_NAME)

    # 11. 验证订单金额
    assert checkout_page.get_subtotal() == BACKPACK_PRICE
    assert checkout_page.get_total() == BACKPACK_TOTAL

    # 12. 点击 Finish，完成订单
    checkout_page.finish_checkout()

    # 13. 验证订单成功
    checkout_page.verify_checkout_complete()