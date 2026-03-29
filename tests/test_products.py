import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.test_data import SEARCH_TERMS


class TestProducts:
    @pytest.mark.smoke
    def test_search_valid_product(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.is_homepage_visible()
        home_page.go_to_products()
        
        search = ProductsPage(driver)
        assert search.is_products_visible()
        search.search(SEARCH_TERMS["valid"])
        assert search.is_searched_products_visible()

        assert  search.has_results()

    def test_search_invalid_product(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.is_homepage_visible()
        home_page.go_to_products()
        
        search = ProductsPage(driver)
        assert search.is_products_visible()
        search.search(SEARCH_TERMS["invalid"])
        assert search.is_searched_products_visible()

        assert not search.has_results()