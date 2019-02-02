import pytest
from selenium import webdriver
from pages.redfin_pages import HomePage


@pytest.fixture
def driver():
	"""Create a webdriver instance for test use."""
	driver = webdriver.Chrome()
	driver.maximize_window()
	yield driver
	driver.quit()


@pytest.fixture
def redfin_homepage(driver):
	"""Navigate to Redfin homepage and return page object."""
	driver.get("https://www.redfin.com")
	homepage = HomePage(driver)
	return homepage
