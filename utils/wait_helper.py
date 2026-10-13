from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:
    """
    Wrapper around Selenium's explicit wait.
    NO time.sleep() anywhere in this framework.
    """

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def all_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def url_contains(self, fragment):
        return self.wait.until(EC.url_contains(fragment))

    def text_in(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))