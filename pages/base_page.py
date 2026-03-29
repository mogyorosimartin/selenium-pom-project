from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)


    COOKIE_CONSENT_BUTTON = (By.CSS_SELECTOR, "button.fc-cta-consent")
    SUBSCRIBE_FIELD = ( By.ID,"susbscribe_email")
    SUBSCRIBE_BUTTON = ( By.ID,"subscribe")
    SUB_SUCCESS = (By.XPATH, "//h2[contains(text(),'You have been successfully subscribed!')]")

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
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

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
        
    def select_dropdown(self, locator, value):
        element = self.find(locator)
        Select(element).select_by_visible_text(value)
        
    def scroll_to_footer(self):
        footer = self.find((By.CSS_SELECTOR, "footer"))
        self.driver.execute_script("arguments[0].scrollIntoView();", footer)
    
    def fill_send_subscribe_form(self, email):
        field = self.find(self.SUBSCRIBE_FIELD)
        field.clear()
        field.send_keys(email)
        self.click(self.SUBSCRIBE_BUTTON)
        
    def sub_success_visible(self):
        return self.is_visible(self.SUB_SUCCESS)
    
    def format_locator(self, locator, *args):
        return (locator[0], locator[1].format(*args))