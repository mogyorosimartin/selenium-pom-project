from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    NAV_LOGIN = (By.LINK_TEXT, "Signup / Login")
    NAV_LOGGED_IN_AS = (By.CSS_SELECTOR, "li a b")
    PRODUCTS_SECTION = (By.CSS_SELECTOR, ".features_items")
    CAROUSEL = (By.ID,"slider-carousel")

    URL = "/"

    def open_home_page(self, base_url):
        self.open(f"{base_url}{self.URL}")

    def go_to_login(self):
        self.click(self.NAV_LOGIN)
        self.wait_for_url("login")

    def search_for(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def get_logged_in_username(self):
        return self.get_text(self.NAV_LOGGED_IN_AS)

    def is_products_section_visible(self):
        return self.is_visible(self.PRODUCTS_SECTION)
    
    def is_homepage_visible(self):
        return self.is_visible(self.CAROUSEL)
    