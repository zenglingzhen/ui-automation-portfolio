
import pytest
import os
import base64
from pytest_html import extras
from test_data import BASE_URL


@pytest.fixture
def app_page(page):
    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000,
    )
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("app_page")

        if page is None:
            page = item.funcargs.get("page")

        if page is not None:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_path = os.path.join(
                screenshot_dir,
                f"{item.name}.png"
            )

            try:
                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )

                print(f"\n失败截图已保存：{screenshot_path}")

                if hasattr(report, "extras"):
                    with open(screenshot_path, "rb") as image_file:
                        image_base64 = base64.b64encode(
                            image_file.read()
                        ).decode("utf-8")

                    report.extras.append(
                        extras.html(
                            f'<div><p>失败截图：</p>'
                            f'<img src="data:image/png;base64,{image_base64}" '
                            f'style="width:600px;"></div>'
                        )
                    )

            except Exception as e:
                print(f"\n截图生成失败：{e}")
