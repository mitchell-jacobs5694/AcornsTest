import pytest
from pages.redfin_pages import HomePage
import time

def test_property_search_with_filters(driver):
	"""Search a city, add filters to search, verify correct results."""
	homepage = HomePage(driver)
	homepage.search_for_city("Gardena")
	time.sleep(3)