import os
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLogin:
    def test_login_with_invalid_credentials(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.login("wrong@email.com", "wrongpassword")

        assert login_page.is_error_displayed()
        assert "incorrect" in login_page.get_error_message().lower()

    def test_login_with_valid_credentials(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.login(
            os.getenv("TEST_EMAIL"),
            os.getenv("TEST_PASSWORD")
        )

        home_page = HomePage(driver)
        home_page.wait_for_url("/")

        username = home_page.get_logged_in_username()
        assert username is not None
        assert len(username) > 0
        
    def test_login_with_empty_fields(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.login("", "")
        assert "login" in driver.current_url
        
    def test_login_with_unregistered_email(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open_login_page(base_url)
        login_page.login("notregistered@example.com", "somepassword")

        assert login_page.is_error_displayed()
        assert "incorrect" in login_page.get_error_message().lower()