from pages.home_page import HomePage
from pages.testcases_page import TCPage

class TestTestCases:
    def test_verify_testcases_page(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.open_home_page(base_url)
        assert home_page.wait_for_homepage()
        home_page.go_to_testcases()
        
        Test_page = TCPage(driver)
        assert Test_page.wait_for_test_cases()