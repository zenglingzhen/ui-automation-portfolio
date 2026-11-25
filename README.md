# UI Automation Testing Portfolio

## 1. Project Overview

This project is a web UI automation testing portfolio built with Python, Playwright, and Pytest.

It uses SauceDemo as the demo application and demonstrates automated testing of core e-commerce workflows.

## 2. Tech Stack

- Python 3.12
- Playwright
- Pytest
- Pytest-HTML
- Page Object Model (POM)

## 3. Project Structure

```text
ui-automation-portfolio/
├── conftest.py
├── test_data.py
├── pytest.ini
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
└── reports/
    ├── report.html
    └── screenshots/
```

## 4. Test Scenarios

### Login
- Valid login
- Invalid username
- Invalid password
- Empty username
- Empty password

### Products
- Verify product list visibility
- Verify product count

### Shopping Cart
- Add one product
- Add multiple products
- Remove a product

### Checkout
- Enter customer information
- Verify order overview
- Verify item subtotal and total
- Complete checkout successfully

## 5. Run Tests

Install dependencies:

```bash
pip install pytest playwright pytest-playwright pytest-html
playwright install chromium
```

Run all tests:

```bash
python -m pytest
```

Generate an HTML report:

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

## 6. Test Report

HTML test reports are generated in the `reports/` directory.

Failed tests automatically save screenshots under `reports/screenshots/`.

## 7. Design Highlights

- Page Object Model for maintainable test code
- Centralized test data management
- Centralized base URL configuration
- Independent test cases
- Automatic HTML reporting
- Screenshot capture for failed tests