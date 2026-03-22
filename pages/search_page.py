from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".productinfo")
    NO_RESULTS_TEXT = (By.CSS_SELECTOR, ".features_items p")

    URL = "/products"

    def open_products_page(self, base_url):
        self.open(f"{base_url}{self.URL}")
        
    def search(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def has_results(self):
        return self.is_visible(self.SEARCH_RESULTS)

    def get_no_results_text(self):
        return self.get_text(self.NO_RESULTS_TEXT)