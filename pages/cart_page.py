from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class CartPage(BasePage):
    """Page Object for the Shopping Cart page."""

    CART_ROWS      = (By.CSS_SELECTOR, "#cart-table tbody tr.cart-row")
    PRODUCT_NAMES  = (By.CSS_SELECTOR, ".product-name")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".product-price")
    PRODUCT_QTY    = (By.CSS_SELECTOR, ".product-qty")
    PRODUCT_TOTALS = (By.CSS_SELECTOR, ".product-total")
    REMOVE_BTNS    = (By.CSS_SELECTOR, ".remove-btn")
    SUBTOTAL       = (By.ID, "subtotal")
    EMPTY_CART     = (By.ID, "empty-cart")
    CHECKOUT_BTN   = (By.ID, "checkout-btn")

    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)
        self.base_url = ConfigReader().get("base_url")

    def open_cart(self):
        self.open(f"{self.base_url}/cart")
        return self

    def get_item_count(self):
        """Returns number of items in cart. Returns 0 if cart is empty."""
        try:
            return len(self.get_elements(self.CART_ROWS))
        except TimeoutException:
            return 0

    def get_product_names(self):
        return [el.text.strip() for el in self.get_elements(self.PRODUCT_NAMES)]

    def get_product_prices(self):
        return [el.text.strip() for el in self.get_elements(self.PRODUCT_PRICES)]

    def get_product_quantities(self):
        return [el.text.strip() for el in self.get_elements(self.PRODUCT_QTY)]

    def get_subtotal(self):
        return self.get_text(self.SUBTOTAL)

    def is_empty(self):
        return self.is_visible(self.EMPTY_CART)

    def remove_first_item(self):
        buttons = self.get_elements(self.REMOVE_BTNS)
        if buttons:
            buttons[0].click()

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)