import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.test_data import SEARCH_TERMS


class TestProducts:
    @pytest.mark.smoke
    def test_search_valid_product(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_products()
        
        search = ProductsPage(driver)
        assert search.wait_for_products()
        search.search(SEARCH_TERMS["valid"])
        assert search.wait_for_searched_products()

        assert  search.has_results()

    def test_search_invalid_product(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_products()
        
        search = ProductsPage(driver)
        assert search.wait_for_products()
        search.search(SEARCH_TERMS["invalid"])
        assert search.wait_for_searched_products()

        assert not search.has_results()