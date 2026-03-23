import os
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.test_data import REGISTER_USER


class TestRegister:
    def test_register_with_valid_info(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.signup_visible()
        login_page.signup(REGISTER_USER["name"], REGISTER_USER["email"])
        register_page = RegisterPage(driver)
        assert register_page.is_account_info_visible()
        register_page.register(REGISTER_USER)
        assert register_page.is_account_created_visible()
        register_page.click_continue()
        assert register_page.is_user_logged_in(REGISTER_USER["name"])
        register_page.delete_account()
        assert register_page.is_account_deleted_visible()
        register_page.click_continue()
        
        