from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:
    """
    Central WebDriver factory.
    Selenium 4.6+ auto-manages browser drivers — no manual setup needed.
    """

    @staticmethod
    def get_driver(browser="chrome", headless=False):
        browser = browser.lower()

        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--log-level=3")
            if headless:
                options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")