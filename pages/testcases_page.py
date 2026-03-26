from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TCPage(BasePage):
    TESTCASES_PROMPT = (By.XPATH, "//b[contains(text(),'Test Cases')]")
    URL = "/test_cases"

    def is_test_cases_visible(self):
        return self.is_visible(self.TESTCASES_PROMPT)