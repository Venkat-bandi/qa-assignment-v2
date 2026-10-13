import time
from behave import given, when, then
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import ConfigReader
from utils.wait_helper import WaitHelper


@given("I open the register page")
def step_open_register(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.open_register()
    assert "/register" in context.driver.current_url, \
        f"Expected /register, got {context.driver.current_url}"


@given("I open the login page")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login()
    assert "/login" in context.driver.current_url, \
        f"Expected /login, got {context.driver.current_url}"


@when('I register with a unique email and password "{password}"')
def step_register_unique(context, password):
    unique_email = f"qa.user.{int(time.time())}@shopqa.com"
    context.registered_email = unique_email
    context.registered_password = password
    context.register_page.register(unique_email, password)


@when('I log in with email "{email}" and password "{password}"')
def step_login_with(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.login(email, password)


@when("I log in with the registered credentials")
def step_login_registered(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login()
    assert "/login" in context.driver.current_url, \
        f"Login page not loaded. URL: {context.driver.current_url}"
    context.login_page.login(context.registered_email, context.registered_password)


@then("I should be redirected to the login page")
def step_on_login(context):
    WaitHelper(context.driver).url_contains("/login")
    assert "/login" in context.driver.current_url, \
        f"Expected /login, got {context.driver.current_url}"


@then("I should see a success message")
def step_success_message(context):
    msg = context.login_page.get_success()
    assert msg is not None, "Success message not displayed"
    assert "successfully" in msg.lower(), \
        f"Expected 'successfully' in message, got: {msg}"


@then("I should land on the products page")
def step_on_products(context):
    WaitHelper(context.driver).url_contains("/products")
    assert "/products" in context.driver.current_url, \
        f"Expected /products, got {context.driver.current_url}"


@then("I should see an error message")
def step_error_message(context):
    msg = context.login_page.get_error()
    assert msg is not None, "Error message not displayed"
    assert "invalid" in msg.lower(), \
        f"Expected 'invalid' in error, got: {msg}"


@given("I am logged in as a test user")
def step_login_test_user(context):
    cfg = ConfigReader()
    email = cfg.get("test_email")
    password = cfg.get("test_password")

    login = LoginPage(context.driver)
    login.open_login()
    assert "/login" in context.driver.current_url, \
        f"Login page not loaded. URL: {context.driver.current_url}"

    try:
        login.login(email, password)
        WaitHelper(context.driver, timeout=4).url_contains("/products")
        assert "/products" in context.driver.current_url, \
            f"Login failed. URL: {context.driver.current_url}"
    except Exception:
        register = RegisterPage(context.driver)
        register.open_register()
        assert "/register" in context.driver.current_url, \
            f"Register page not loaded. URL: {context.driver.current_url}"
        register.register(email, password)

        login.open_login()
        assert "/login" in context.driver.current_url, \
            f"Login page not loaded after register. URL: {context.driver.current_url}"
        login.login(email, password)
        WaitHelper(context.driver).url_contains("/products")
        assert "/products" in context.driver.current_url, \
            f"Login failed after register. URL: {context.driver.current_url}"