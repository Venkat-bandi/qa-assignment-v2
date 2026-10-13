from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class OrdersPage(BasePage):
    """Page Object for the Orders page."""

    # Locators
    ORDER_CARDS  = (By.CSS_SELECTOR, ".order-card")
    ORDER_IDS    = (By.CSS_SELECTOR, ".order-id")
    ORDER_TOTALS = (By.CSS_SELECTOR, ".order-total")
    ORDER_DATES  = (By.CSS_SELECTOR, ".order-date")
    NO_ORDERS    = (By.ID, "no-orders")

    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)
        self.base_url = ConfigReader().get("base_url")

    def open_orders(self):
        self.open(f"{self.base_url}/orders")
        return self

    def get_order_count(self):
        return len(self.get_elements(self.ORDER_CARDS))

    def get_order_ids(self):
        return [el.text.strip() for el in self.get_elements(self.ORDER_IDS)]

    def get_order_totals(self):
        return [el.text.strip() for el in self.get_elements(self.ORDER_TOTALS)]

    def is_empty(self):
        return self.is_visible(self.NO_ORDERS)