from pages.contact_page import ContactPage
from utils.test_data import CONTACT_FORM
from pages.home_page import HomePage
import os

class TestContact:
    def test_contact_form_submission(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.is_homepage_visible()
        home_page.go_to_contact()
        contact = ContactPage(driver)
        assert contact.is_visible_getintouch()
        contact.fill_form(
            CONTACT_FORM["name"],
            CONTACT_FORM["email"],
            CONTACT_FORM["subject"],
            CONTACT_FORM["message"]
        )
        file_path = os.path.join(os.path.dirname(__file__), "assets", "sample.png")
        contact.file_upload(file_path)
        contact.submit_form()
        driver.switch_to.alert.accept()
        assert contact.is_success_message_visible()