from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    """Wait until element is visible and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_clickable(driver, locator, timeout=10):
    """Wait until element is clickable and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_for_url_contains(driver, text, timeout=10):
    """Wait until URL contains expected text."""
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(text)
    )