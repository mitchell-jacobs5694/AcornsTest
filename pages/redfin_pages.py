from selenium.webdriver.support.ui import Select
from common.base import BasePage, MultiPageElement, PageElement
from locators import HomePageLocators, SearchResultsPageLocators


class HomePage(BasePage):
	"""Redfin Homepage."""

	city_search_input_box = PageElement(HomePageLocators.CITY_SEARCH_INPUT)
	city_search_button = PageElement(HomePageLocators.CITY_SEARCH_BUTTON)

	def search_for_city(self, city):
		"""Input city name into search bar and click 'Search'."""
		self.city_search_input_box.wait_for_visibility()
		self.city_search_input_box = city
		self.city_search_button.click()
		return SearchResultsPage(self.driver)


class SearchResultsPage(BasePage):
	"""Redfin Search results page."""

	apply_filters_button = PageElement(SearchResultsPageLocators.APPLY_FILTERS)
	max_bedroom_select = PageElement(SearchResultsPageLocators.MAX_BEDS)
	max_price_select = PageElement(SearchResultsPageLocators.MAX_PRICE)
	max_square_foot = PageElement(SearchResultsPageLocators.MAX_FEET)
	min_bedroom_select = PageElement(SearchResultsPageLocators.MIN_BEDS)
	min_price_select = PageElement(SearchResultsPageLocators.MIN_PRICE)
	min_square_foot = PageElement(SearchResultsPageLocators.MIN_FEET)
	more_filters_button = PageElement(SearchResultsPageLocators.MORE_FILTERS)
	results_list = MultiPageElement(SearchResultsPageLocators.RESULTS_LIST)
	results_table_option = PageElement(SearchResultsPageLocators.RESULTS_TABLE)

	def _make_visible(self, element):
		"""Remove 'None' display style of element.

		Used to enable automation on hidden Select elements.
		"""
		self.driver.execute_script(
			"arguments[0].style.display = 'block';", element)

	def _set_select_value(self, select_element, value):
		"""Select value from Select HTML element."""
		select = Select(select_element)
		select.select_by_value(value)

	def set_range_filter(self, range_name, filter_values):
		"""Set specified range filter field to given values."""
		filters = {
			"beds":{
				"max": self.max_bedroom_select,
				"min": self.min_bedroom_select,
				},
			"price": {
				"max": self.max_price_select,
				"min": self.min_price_select,
				},
			"square_foot": {
				"max": self.max_square_foot,
				"min": self.min_square_foot,
				}}

		range_elements = filters[range_name]
		for range_name in ['min', 'max']:
			self._make_visible(range_elements[range_name])
			self._set_select_value(range_elements[range_name],
				filter_values[range_name])

	def open_filters(self):
		"""Click "More Filters" to open filter tab."""
		self.more_filters_button.wait_for_visibility().click()

	def apply_filters(self):
		"""Click the 'Apply Filters' button."""
		self.apply_filters_button.click()

	def switch_to_results_table(self):
		"""Click table button to swicth from pictures to table."""
		self.results_table_option.wait_for_visibility().click()

	def search_results_table_list(self):
		"""Return values for each element in visible search results list."""
		results = []

		for result in self.results_list.elements:
			result_data = {
				"address": result.find_element(
					*SearchResultsPageLocators.RESULT_ADDRESS)
						.get_attribute('title'),
				"beds": int(result.find_element(
					*SearchResultsPageLocators.RESULT_BEDS).text),
				"square_foot": int(result.find_element(
					*SearchResultsPageLocators.RESULT_SQ_FEET).text.replace(
						',', '')),
			}

			price = result.find_element(
				*SearchResultsPageLocators.RESULT_PRICE).text
			for char in [',', '$']:
				price = price.replace(char, '')
			result_data['price'] = int(price)

			results.append(result_data)
		return results
