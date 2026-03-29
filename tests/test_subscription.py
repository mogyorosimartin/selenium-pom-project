from pages.home_page import HomePage
from utils.test_data import EMAIL


class TestSubscription:
    def test_verify_subscription_homepage(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.scroll_to_footer()
        home_page.fill_send_subscribe_form(EMAIL["email"])
    
    def test_verify_subscription_cartpage(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_cart()
        home_page.scroll_to_footer()
        home_page.fill_send_subscribe_form(EMAIL["email"])
        