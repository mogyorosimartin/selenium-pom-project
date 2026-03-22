from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)


    COOKIE_CONSENT_BUTTON = (By.CSS_SELECTOR, "button.fc-cta-consent")

    def open(self, url):
        self.driver.get(url)        
        self._dismiss_cookie_consent()
        
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def wait_for_url(self, partial_url):
        self.wait.until(EC.url_contains(partial_url))

    def _dismiss_cookie_consent(self):
        try:
            consent_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.fc-cta-consent")
                )
            )
            consent_btn.click()
        except TimeoutException:
            pass