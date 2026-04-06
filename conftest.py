import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def dash_duo_browser_options(options):
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return options


@pytest.fixture(scope="session", autouse=True)
def setup_chromedriver():
    driver_path = ChromeDriverManager().install()
    import os

    os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
