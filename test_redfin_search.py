import pytest
import time


@pytest.mark.parametrize('city_search_name,city_title,filters', [
	("Gardena, CA, USA",
	 "Gardena, CA",
	 {"beds": {"max": "2",
	 	  	   "min": "1"},
	  "price": {"max": "550000",
				"min": "100000"},
	  "square_foot": {"max": "1750",
	  				  "min": "750"},
	 }
)])
def test_property_search_with_range_filters(redfin_homepage, city_search_name,
											city_title, filters):
	"""Search a city, add filters to search, verify correct results."""
	search_results_page = redfin_homepage.search_for_city(city_search_name)

	search_results_page.open_filters()
	for filter_name, filter_values in filters.items():
		search_results_page.set_range_filter(filter_name, filter_values)
	search_results_page.apply_filters()
	search_results_page.switch_to_results_table()
	results = search_results_page.search_results_table_list()

	for result in results:
		assert city_title in result['address']
		for filter_name, filter_range in filters.items():
			assert int(filter_range['min']) <= result[filter_name], (
				f"{filter_name} min value is out of range."
				f"\nFilter Value: {filter_range['min']}"
				f"\nSearch Result Value: result[filter_name]")
			assert int(filter_range['max']) >= result[filter_name], (
				f"{filter_name} max value is out of range."
				f"\nFilter Value: {filter_range['max']}"
				f"\nSearch Result Value: result[filter_name]")
