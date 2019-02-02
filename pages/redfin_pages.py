from selenium.webdriver.support.ui import Select
from common.base import BasePage, PageElement
from locators import HomePageLocators, SearchResultsPageLocators


class HomePage(BasePage):
	"""Redfin Homepage."""

	city_search_input_box = PageElement(HomePageLocators.CITY_SEARCH_INPUT)
	city_search_button = PageElement(HomePageLocators.CITY_SEARCH_BUTTON)

	def search_for_city(self, city_name):
		"""Input city name into search bar and click 'Search'."""
		self.city_search_input_box = city_name
		self.city_search_button.click()
		return SearchResultsPage(self.driver)


class SearchResultsPage(BasePage):
	"""Redfin Search results page."""

	max_bedroom_select = PageElement(SearchResultsPageLocators.MAX_BEDS)
	max_price_select = PageElement(SearchResultsPageLocators.MAX_PRICE)
	min_bedroom_select = PageElement(SearchResultsPageLocators.MIN_BEDS)
	min_price_select = PageElement(SearchResultsPageLocators.MIN_PRICE)
	more_filters_button = PageElement(SearchResultsPageLocators.MORE_FILTERS)

	def _make_visible(self, element):
		"""Remove None display style of element.

		Used to enable automation on hidden Select elements.
		"""
		self.driver.execute_script(
			"arguments[0].style.display = 'block';", element)

	def _set_select_value(self, field, value):
		"""Select value from Select HTML element."""
		select = Select(field)
		select.select_by_value(value)

	def set_filter(self, field_name, value):
		"""Set specified filter to given value."""
		filters = {
			"max_beds": self.set_max_bedrooms,
			"max_price": self.set_max_price,
			"min_beds": self.set_min_bedrooms,
			"min_price": self.set_min_price,
			}
		filters[field_name](value)

	def set_max_bedrooms(self, value):
		"""Set the max bedroom filter."""
		self._make_visible(self.max_bedroom_select)
		self._set_select_value(self.max_bedroom_select, value)

	def set_max_price(self, value):
		"""Set the max price filter."""
		self._make_visible(self.max_price_select)
		self._set_select_value(self.max_price_select, value)

	def set_min_bedrooms(self, value):
		"""Set minimum bedroom filter."""
		self._make_visible(self.min_bedroom_select)
		self._set_select_value(self.min_bedroom_select, value)

	def set_min_price(self, value):
		"""Set the minimum price filter."""
		self._make_visible(self.min_price_select)
		self._set_select_value(self.min_price_select, value)

	def open_filters(self):
		"""Click "More Filters" to open filter tab."""
		self.more_filters_button.click()
