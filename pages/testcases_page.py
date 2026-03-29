from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TCPage(BasePage):
    TESTCASES_PROMPT = (By.XPATH, "//b[contains(text(),'Test Cases')]")
    URL = "/test_cases"

    def wait_for_test_cases(self):
        return self.find(self.TESTCASES_PROMPT)