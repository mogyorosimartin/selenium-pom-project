import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.test_data import REGISTER_USER
from utils.test_data import EXISTING_EMAIL


class TestRegister:
    @pytest.mark.smoke
    def test_register_with_valid_info(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        assert login_page.wait_for_signup()
        login_page.signup(REGISTER_USER["name"], REGISTER_USER["email"])
        register_page = RegisterPage(driver)
        register_page.wait_for_signup_page()
        assert register_page.wait_for_account_info()
        register_page.register(REGISTER_USER)
        register_page.click_continue()
        assert register_page.is_user_logged_in(REGISTER_USER["name"])
        register_page.delete_account()
        assert register_page.wait_for_account_deleted()
        register_page.click_continue()
        
    def test_register_with_an_existing_email(self,driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_login()
        
        login_page = LoginPage(driver)
        assert login_page.wait_for_signup()
        login_page.signup(REGISTER_USER["name"],EXISTING_EMAIL)
        assert login_page.wait_for_error()
        assert "Email Address already exist!" in login_page.get_error_message()