
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_products_display_after_login(app_page):
    # 登录
    login_page = LoginPage(app_page)
    login_page.login("standard_user", "secret_sauce")

     # 创建商品页面对象
    products_page = ProductsPage(app_page)

    # 验证进入商品列表页
    expect(app_page).to_have_url(re.compile(r".*/inventory.html"))

    # 验证商品列表显示
    products_page.verify_product_list_visible()

    # 验证商品数量
    assert products_page.get_product_count() == 6
