from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p[style*='color: red']")
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    LOGIN_PROMPT = (By.XPATH, "//h2[contains(text(),'Login to your account')]")
    SIGNUP_PROMPT = (By.XPATH, "//h2[contains(text(),'New User Signup!')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Logout')]")

    URL = "/login"

    def open_login_page(self, base_url):
        self.open(f"{base_url}{self.URL}")

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def signup(self, name, email):
        self.type(self.SIGNUP_NAME, name)
        self.type(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)
    
    def wait_for_signup(self):
        return self.find(self.SIGNUP_PROMPT)


    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def wait_for_error(self):
        return self.find(self.ERROR_MESSAGE)
    
    def wait_for_Login_Prompt(self):
        return self.find(self.LOGIN_PROMPT)
    
    def logout(self):
        self.click(self.LOGOUT_BUTTON)