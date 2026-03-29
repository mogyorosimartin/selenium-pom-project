import os

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLogin:
    def test_login_with_invalid_credentials(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_login()
        
        login_page = LoginPage(driver)
        assert login_page.wait_for_Login_Prompt()
        login_page.login("wrong@email.com", "wrongpassword")

        assert login_page.wait_for_error()
        assert "incorrect" in login_page.get_error_message().lower()
    @pytest.mark.smoke
    def test_login_with_valid_credentials(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_login()
        
        login_page = LoginPage(driver)
        assert login_page.wait_for_Login_Prompt()
        login_page.login(
            os.getenv("TEST_EMAIL"),
            os.getenv("TEST_PASSWORD")
        )
        
        home_page.wait_for_url("/")
        username = home_page.get_logged_in_username()
        assert username is not None
        assert len(username) > 0
        # Note: Official TC2 includes account deletion as cleanup after registration.
        # This suite uses a persistent test account so deletion is omitted here.
        # Account deletion is covered in test_register.py which creates and deletes
        # a fresh account each run.
        
    def test_login_with_empty_fields(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.login("", "")
        assert "login" in driver.current_url
        
    def test_login_with_unregistered_email(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.login("notregistered@example.com", "somepassword")

        assert login_page.wait_for_error()
        assert "incorrect" in login_page.get_error_message().lower()
        
    def test_login_logout(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_login()
        
        login_page = LoginPage(driver)
        assert login_page.wait_for_Login_Prompt()
        login_page.login(
            os.getenv("TEST_EMAIL"),
            os.getenv("TEST_PASSWORD")
        )
        
        home_page.wait_for_url("/")
        username = home_page.get_logged_in_username()
        assert username is not None
        assert len(username) > 0
        
        login_page.logout()
        assert login_page.wait_for_Login_Prompt()