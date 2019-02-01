import pytest
from selenium import webdriver

@pytest.fixture
def driver():
	"""Create a webdriver instance for test use."""
	driver = webdriver.Chrome()
	driver.get("https://www.redfin.com")
	yield driver
	driver.quit()