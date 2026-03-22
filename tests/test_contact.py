from pages.contact_page import ContactPage
from utils.test_data import CONTACT_FORM


class TestContact:
    def test_contact_form_submission(self, driver, base_url):
        contact = ContactPage(driver)
        contact.open_contact_page(base_url)
        contact.submit_form(
            CONTACT_FORM["name"],
            CONTACT_FORM["email"],
            CONTACT_FORM["subject"],
            CONTACT_FORM["message"]
        )
        driver.switch_to.alert.accept()
        assert contact.is_success_message_visible()