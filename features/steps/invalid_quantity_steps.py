from behave import then
from pages.products_page import ProductsPage


@then("I should be on the products page")
def step_on_products(context):
    assert "/products" in context.driver.current_url, \
        f"Expected /products, got {context.driver.current_url}"


@then("I should see a quantity error")
def step_qty_error(context):
    page = ProductsPage(context.driver)
    assert page.is_qty_error(), "Quantity error banner not visible"