import pytest
import time


@pytest.mark.parametrize('city_to_search,filters', [
	("Gardena, CA, USA",
	 {"max_beds": "2",
	  "max_price": "350000",
	  "min_beds": "1",
	  "min_price": "100000",
	  }
)])
def test_property_search_with_filters(redfin_homepage, city_to_search, filters):
	"""Search a city, add filters to search, verify correct results."""
	search_results_page = redfin_homepage.search_for_city(city_to_search)

	search_results_page.open_filters()
	for filter_name, value in filters.items():
		search_results_page.set_filter(filter_name, value)
