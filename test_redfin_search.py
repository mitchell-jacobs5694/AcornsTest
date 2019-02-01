import pytest
import time


@pytest.mark.parametrize('city_to_search', ['Gardena, CA, US'])
def test_property_search_with_filters(redfin_homepage, city_to_search):
	"""Search a city, add filters to search, verify correct results."""
	redfin_homepage.search_for_city(city_to_search)
	time.sleep(3)