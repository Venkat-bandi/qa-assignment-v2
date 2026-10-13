from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Page Object for the Register page."""

    # Locators
    EMAIL_INPUT     = (By.ID, "reg-email")
    PASSWORD_INPUT  = (By.ID, "reg-password")
    CONFIRM_INPUT   = (By.ID, "reg-confirm")
    REGISTER_BUTTON = (By.ID, "register-btn")
    ERROR_MESSAGE   = (By.ID, "register-error")
    LOGIN_LINK      = (By.LINK_TEXT, "Sign in")

    def open_register(self):
        self.open(f"{self._base()}/register")
        return self

    def register(self, email, password, confirm=None):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.type_text(self.CONFIRM_INPUT, confirm if confirm else password)
        self.click(self.REGISTER_BUTTON)

    def get_error(self):
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None

    def _base(self):
        from utils.config_reader import ConfigReader
        return ConfigReader().get("base_url")