import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.test_data import SEARCH_TERMS


class TestSearch:
    def test_search_valid_product(self, driver, base_url):
        search = SearchPage(driver)
        search.open_products_page(base_url)

        search.search(SEARCH_TERMS["valid"])

        assert search.has_results()

    def test_search_invalid_product(self, driver, base_url):
        search = SearchPage(driver)
        search.open_products_page(base_url)
        search.search(SEARCH_TERMS["invalid"])

        assert not search.has_results()