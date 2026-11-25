
import re
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from test_data import STANDARD_USER, PASSWORD


def test_valid_login(app_page):
    #创建登录对象
    login_page =LoginPage(app_page)

    #执行登录
    # login_page.login("standard_user","secret_sauce")
    login_page.login(STANDARD_USER, PASSWORD)
    #验证登录成功

    expect(app_page).to_have_url(
        re.compile(r".*/inventory.html")
    )
    expect(app_page.locator(".inventory_list")).to_be_visible()

@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        (STANDARD_USER, "wrong_password",
         "Username and password do not match"),
        ("invalid_user", PASSWORD,
         "Username and password do not match"),
        ("", PASSWORD,
         "Username is required"),
        (STANDARD_USER, "",
         "Password is required"),
    ]
)

def test_invalid_login(app_page, username, password, expected_message):

    #创建登录对象
    login_page =LoginPage(app_page)

     #使用错误密码登录
    login_page.login(username, password)

    #验证错误提示
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(expected_message)
