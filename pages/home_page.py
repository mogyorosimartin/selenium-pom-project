from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    NAV_LOGIN = (By.LINK_TEXT, "Signup / Login")
    NAV_CONTACT =(By.LINK_TEXT, "Contact us")
    NAV_CART =(By.XPATH, '//a[@href="/view_cart"]')
    NAV_TESTCASES =(By.LINK_TEXT, "Test Cases")
    NAV_PRODUCTS =(By.XPATH, '//a[@href="/products"]')
    NAV_LOGGED_IN_AS = (By.CSS_SELECTOR, "li a b")
    PRODUCTS_SECTION = (By.CSS_SELECTOR, ".features_items")
    CAROUSEL = (By.ID,"slider-carousel")

    URL = "/"

    def open_home_page(self, base_url):
        self.open(f"{base_url}{self.URL}")

    def go_to_login(self):
        self.click(self.NAV_LOGIN)
        self.wait_for_url("login")
        
    def go_to_contact(self):
        self.click(self.NAV_CONTACT)
        self.wait_for_url("contact_us")
        
    def go_to_cart(self):
        self.click(self.NAV_CART)
        self.wait_for_url("view_cart")
    
    def go_to_testcases(self):
        self.click(self.NAV_TESTCASES)
        self.wait_for_url("test_cases")
        
    def go_to_products(self):
        self.click(self.NAV_PRODUCTS)
        self.wait_for_url("products")

    def search_for(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def get_logged_in_username(self):
        return self.get_text(self.NAV_LOGGED_IN_AS)

    def is_products_section_visible(self):
        return self.is_visible(self.PRODUCTS_SECTION)
    
    def is_homepage_visible(self):
        return self.is_visible(self.CAROUSEL)
    