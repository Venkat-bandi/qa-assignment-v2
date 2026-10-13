from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class CheckoutPage(BasePage):
    """Page Object for the Checkout page."""

    # Locators
    COUPON_INPUT   = (By.ID, "coupon-input")
    APPLY_COUPON   = (By.ID, "apply-coupon")
    COUPON_MSG     = (By.ID, "coupon-msg")
    SUBTOTAL       = (By.ID, "subtotal")
    DISCOUNT       = (By.ID, "discount")
    TOTAL          = (By.ID, "total")
    PLACE_ORDER    = (By.ID, "place-order")

    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)
        self.base_url = ConfigReader().get("base_url")

    def open_checkout(self):
        self.open(f"{self.base_url}/checkout")
        return self

    def apply_coupon(self, code):
        self.type_text(self.COUPON_INPUT, code)
        self.click(self.APPLY_COUPON)

    def get_coupon_message(self):
        if self.is_visible(self.COUPON_MSG):
            return self.get_text(self.COUPON_MSG)
        return None

    def get_subtotal(self):
        return self.get_text(self.SUBTOTAL)

    def get_discount(self):
        return self.get_text(self.DISCOUNT)

    def get_total(self):
        return self.get_text(self.TOTAL)

    def place_order(self):
        self.click(self.PLACE_ORDER)