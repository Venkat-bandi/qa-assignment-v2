from behave import when, then
from pages.checkout_page import CheckoutPage
from pages.orders_page import OrdersPage


@when("I open the checkout page")
def step_open_checkout(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.open_checkout()
    assert "/checkout" in context.driver.current_url, \
        f"Checkout page not loaded. URL: {context.driver.current_url}"


@when('I apply the coupon "{code}"')
def step_apply_coupon(context, code):
    context.checkout_page.apply_coupon(code)


@when("I place the order")
def step_place_order(context):
    context.checkout_page.place_order()


@then("the coupon should be accepted")
def step_coupon_accepted(context):
    msg = context.checkout_page.get_coupon_message()
    assert msg is not None, "No coupon message displayed"
    assert "applied" in msg.lower(), \
        f"Expected 'applied' in message, got: {msg}"


@then("the coupon should be rejected")
def step_coupon_rejected(context):
    msg = context.checkout_page.get_coupon_message()
    assert msg is not None, "No coupon message displayed"
    msg_lower = msg.lower()
    assert "expired" in msg_lower or "invalid" in msg_lower, \
        f"Expected 'expired' or 'invalid' in message, got: {msg}"


@then('the discount should not be "{value}"')
def step_discount_not(context, value):
    actual = context.checkout_page.get_discount().strip()
    assert actual != value, f"Discount was unexpectedly '{value}'"


@then('the discount should be "{value}"')
def step_discount_is(context, value):
    actual = context.checkout_page.get_discount().strip()
    assert actual == value, f"Expected discount '{value}', got '{actual}'"


@then("I should land on the orders page")
def step_on_orders(context):
    assert "/orders" in context.driver.current_url, \
        f"Expected /orders, got {context.driver.current_url}"


@then("I should see at least {count:d} order")
def step_orders_count(context, count):
    page = OrdersPage(context.driver)
    actual = page.get_order_count()
    assert actual >= count, f"Expected at least {count} order(s), got {actual}"


@then("I should see at least {count:d} orders")
def step_orders_count_plural(context, count):
    page = OrdersPage(context.driver)
    actual = page.get_order_count()
    assert actual >= count, f"Expected at least {count} order(s), got {actual}"