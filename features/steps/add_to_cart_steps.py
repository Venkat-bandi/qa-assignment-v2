from behave import given, when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@given('I have added "{product}" to cart with quantity {qty:d}')
def step_given_add_named(context, product, qty):
    context.products_page = ProductsPage(context.driver)
    context.products_page.open_products()
    assert "/products" in context.driver.current_url, \
        f"Products page not loaded. URL: {context.driver.current_url}"
    context.products_page.search(product)
    context.products_page.add_first_to_cart(qty)


@when('I search for "{term}"')
def step_search(context, term):
    context.products_page = ProductsPage(context.driver)
    context.products_page.search(term)
    assert context.products_page.get_product_count() > 0, \
        f"No products found for '{term}'"


@when("I open the products page")
def step_open_products(context):
    context.products_page = ProductsPage(context.driver)
    context.products_page.open_products()
    assert "/products" in context.driver.current_url, \
        f"Products page not loaded. URL: {context.driver.current_url}"
    assert context.products_page.get_product_count() > 0, \
        "No products listed on products page"


@when('I add the first product to cart with quantity {qty:d}')
def step_add_first(context, qty):
    if not hasattr(context, "products_page"):
        context.products_page = ProductsPage(context.driver)
    context.products_page.add_first_to_cart(qty)


@when('I add the first product to cart with quantity "{qty}"')
def step_add_first_str(context, qty):
    if not hasattr(context, "products_page"):
        context.products_page = ProductsPage(context.driver)
    context.products_page.add_first_to_cart(qty)


@when("I open the cart page")
def step_open_cart(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.open_cart()
    assert "/cart" in context.driver.current_url, \
        f"Cart page not loaded. URL: {context.driver.current_url}"


@then("the cart should contain {count:d} item")
def step_cart_count(context, count):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    actual = context.cart_page.get_item_count()
    assert actual == count, f"Expected {count} item(s), got {actual}"


@then("the cart should contain {count:d} items")
def step_cart_count_plural(context, count):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    actual = context.cart_page.get_item_count()
    assert actual == count, f"Expected {count} item(s), got {actual}"


@then('the cart should display "{product}"')
def step_cart_displays(context, product):
    names = context.cart_page.get_product_names()
    assert len(names) > 0, "Cart has no product names to verify"
    found = any(product.lower() in n.lower() for n in names)
    assert found, f"'{product}' not in cart. Cart has: {names}"


@then('the quantity of the first product should be "{qty}"')
def step_first_qty(context, qty):
    quantities = context.cart_page.get_product_quantities()
    assert len(quantities) > 0, "No products in cart"
    assert quantities[0] == qty, f"Expected qty '{qty}', got '{quantities[0]}'"