from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):
    """Page Object for the Login page."""

    EMAIL_INPUT    = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-btn")
    ERROR_MESSAGE  = (By.ID, "login-error")
    SUCCESS_MSG    = (By.ID, "login-success")

    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)
        self.base_url = ConfigReader().get("base_url")

    def open_login(self):
        self.open(f"{self.base_url}/login")
        return self

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error(self):
        try:
            self.wait.visible(self.ERROR_MESSAGE)
            return self.get_text(self.ERROR_MESSAGE)
        except TimeoutException:
            return None

    def get_success(self):
        try:
            self.wait.visible(self.SUCCESS_MSG)
            return self.get_text(self.SUCCESS_MSG)
        except TimeoutException:
            return None