from pages.cart_page import CartPage
from pages.home_page import HomePage


class TestCart:
    def test_cart_add_product(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.is_homepage_visible()
        home_page.go_to_products()
        
        cart_page = CartPage(driver)
        cart_page.add_to_cart(1)
        cart_page.click_continue()
        cart_page.add_to_cart(2)
        cart_page.click_cart()
        cart_page.verify_cart(2)
        