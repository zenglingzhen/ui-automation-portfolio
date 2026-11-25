
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # 登录页面元素
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    # 登录操作
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
