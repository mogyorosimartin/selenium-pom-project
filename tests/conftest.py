import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    # SETUP
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--block-new-web-contents")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.ads": 2,
    })
    options.add_argument("--headless=new")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10) 
    yield driver 
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://automationexercise.com")