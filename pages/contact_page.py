from selenium.webdriver.common.by import By
from pages.base_page import BasePage





class ContactPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Success! Your details have been submitted successfully.')]")
    GETINTOUCH_MESSAGE = (By.XPATH, "//h2[contains(text(),'Get In Touch')]")
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")

    URL = "/contact_us"
    
    def open_contact_page(self, base_url):
        self.open(f"{base_url}{self.URL}")

    def fill_form(self, name, email, subject, message):
        self.type(self.NAME_INPUT, name)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.SUBJECT_INPUT, subject)
        self.type(self.MESSAGE_INPUT, message)
        
    def submit_form(self ):
        self.click(self.SUBMIT_BUTTON)

    def wait_for_success_message(self):
        return self.find(self.SUCCESS_MESSAGE)
    
    def wait_for_getintouch(self):
        return self.find(self.GETINTOUCH_MESSAGE)
    
    def file_upload(self, file_path):
        self.driver.find_element(*self.FILE_INPUT).send_keys(file_path)
