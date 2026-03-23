from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    ENTER_ACCOUNT_TITLE = (By.XPATH, "/html/body/section/div/div/div/div/h2/b")
    TITLE_GENDER2 = (By.ID, "id_gender2")
    TITLE_GENDER1 = (By.ID, "id_gender1")    
    REGISTER_NAME = (By.ID, "name")
    REGISTER_EMAIL = (By.ID, "email")
    REGISTER_PASSWORD = (By.ID, "password") 
    BIRTHDAY_DAY = (By.ID, "days")
    BIRTHDAY_MONTH = (By.ID, "months")
    BIRTHDAY_YEAR = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIALOFFER_CHECKBOX = (By.ID, "optin")
    REGISTER_FIRSTNAME = (By.ID, "first_name")
    REGISTER_LASTNAME = (By.ID, "last_name")
    REGISTER_ADDRESS1 = (By.ID, "address1")
    REGISTER_ADDRESS2 = (By.ID, "address2")
    REGISTER_COUNTRYLIST = (By.ID, "country")
    REGISTER_STATE = (By.ID, "state")
    REGISTER_CITY = (By.ID, "city")
    REGISTER_ZIPCODE = (By.ID, "zipcode")
    REGISTER_MOBILE = (By.ID, "mobile_number")    
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED_TEXT = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    LOGGED_IN = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
    DELETE_BTN = (By.CSS_SELECTOR, ".fa.fa-trash-o")
    ACCOUNT_DELETED = (By.XPATH, "/html/body/section/div/div/div/h2/b")
    

    URL = "/signup"

    def open_register_page(self, base_url):
        self.open(f"{base_url}{self.URL}")

    def register(self, user_data):
        if (user_data["title"] == 1):
            self.click(self.TITLE_GENDER1)
        else:
            self.click(self.TITLE_GENDER2)
        self.type(self.REGISTER_NAME,user_data["name"])
        self.type(self.REGISTER_PASSWORD,user_data["password"])
        self.select_dropdown(self.BIRTHDAY_DAY, user_data["day"])
        self.select_dropdown(self.BIRTHDAY_MONTH, user_data["month"])
        self.select_dropdown(self.BIRTHDAY_YEAR, user_data["year"])
        if user_data["newsletter"]:
            self.click(self.NEWSLETTER_CHECKBOX)
        if user_data["optin"]:
            self.click(self.SPECIALOFFER_CHECKBOX)
        self.type(self.REGISTER_FIRSTNAME,user_data["first_name"])
        self.type(self.REGISTER_LASTNAME,user_data["last_name"])
        self.type(self.REGISTER_ADDRESS1,user_data["address1"])
        self.type(self.REGISTER_ADDRESS2,user_data["address2"])
        self.select_dropdown(self.REGISTER_COUNTRYLIST, user_data["country"])
        self.type(self.REGISTER_STATE,user_data["state"])
        self.type(self.REGISTER_CITY,user_data["city"])
        self.type(self.REGISTER_ZIPCODE,user_data["zipcode"])
        self.type(self.REGISTER_MOBILE,user_data["mobile_number"])
        self.click(self.SIGNUP_BUTTON)
        
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)
    
    def is_account_info_visible(self):
        return self.is_visible(self.ENTER_ACCOUNT_TITLE)
    
    
    def is_account_created_visible(self):
        return self.is_visible(self.ACCOUNT_CREATED_TEXT)
    
    def is_user_logged_in(self):
        return self.is_visible(self.LOGGED_IN)
    
    def delete_account(self):
        self.click(self.DELETE_BTN)
        
    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED)
    
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    
