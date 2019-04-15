import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from core.page_manager import PageManager


@pytest.yield_fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.fullscreen_window()
    yield driver
    driver.quit()


@pytest.yield_fixture()
def pm(driver):
    pm = PageManager(driver)
    yield pm
