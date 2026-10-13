from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class ProductsPage(BasePage):
    """Page Object for the Products listing page."""

    SEARCH_INPUT    = (By.ID, "search")
    SEARCH_BUTTON   = (By.ID, "search-btn")
    PRODUCT_CARDS   = (By.CSS_SELECTOR, ".product-card")
    PRODUCT_NAMES   = (By.CSS_SELECTOR, ".product-name")
    PRODUCT_PRICES  = (By.CSS_SELECTOR, ".product-price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart")
    QTY_INPUTS      = (By.CSS_SELECTOR, ".qty-input")
    NO_RESULTS      = (By.ID, "no-results")
    QTY_ERROR       = (By.ID, "qty-error")

    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)
        self.base_url = ConfigReader().get("base_url")

    def open_products(self):
        self.open(f"{self.base_url}/products")
        return self

    def search(self, term):
        self.open_products()
        self.type_text(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)
        self.wait.all_present(self.PRODUCT_CARDS)

    def get_first_product_name(self):
        return self.get_text(self.PRODUCT_NAMES)

    def get_first_product_price(self):
        return self.get_text(self.PRODUCT_PRICES)

    def get_product_names(self):
        return [el.text.strip() for el in self.get_elements(self.PRODUCT_NAMES)]

    def get_product_count(self):
        return len(self.get_elements(self.PRODUCT_CARDS))

    def add_first_to_cart(self, qty=1):
        """Adds the first product to cart. Uses JS to force qty (bypasses HTML min/max)."""
        self.wait.all_present(self.PRODUCT_CARDS)

        self.driver.execute_script("""
            const card = document.querySelector('.product-card');
            const input = card.querySelector('.qty-input');
            input.value = arguments[0];
        """, str(qty))

        add_btn = self.driver.find_element(
            By.CSS_SELECTOR, ".product-card:first-of-type .add-to-cart"
        )
        self.driver.execute_script("arguments[0].click();", add_btn)

    def is_no_results(self):
        return self.is_visible(self.NO_RESULTS)

    def is_qty_error(self):
        return self.is_visible(self.QTY_ERROR)