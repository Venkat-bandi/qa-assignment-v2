import time
from utils.wait_helper import WaitHelper


class BasePage:
    """
    Parent class for all page objects.
    Uses explicit waits + human-like pause so the flow is visible.
    """

    SLOW_MODE = True
    PAUSE = 2.0

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WaitHelper(driver, timeout)

    def _pause(self):
        if self.SLOW_MODE:
            time.sleep(self.PAUSE)

    def open(self, url):
        self.driver.get(url)
        self._pause()

    def click(self, locator):
        self.wait.clickable(locator).click()
        self._pause()

    def type_text(self, locator, text):
        element = self.wait.visible(locator)
        element.clear()
        element.send_keys(text)
        self._pause()

    def get_text(self, locator):
        return self.wait.visible(locator).text.strip()

    def is_visible(self, locator):
        try:
            self.wait.visible(locator)
            return True
        except Exception:
            return False

    def get_elements(self, locator):
        return self.wait.all_present(locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def dismiss_ads(self):
        try:
            self.driver.execute_script("""
                document.querySelectorAll('iframe[id^="aswift"], iframe[name^="aswift"]')
                    .forEach(el => el.remove());
            """)
        except Exception:
            pass