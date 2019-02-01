from common.base import BasePage, PageElement
from locators import HomePageLocators

class HomePage(BasePage):
	"""Redfin Homepage."""
	
	city_search_input_box = PageElement(HomePageLocators.CITY_SEARCH_INPUT)
	city_search_button = PageElement(HomePageLocators.CITY_SEARCH_BUTTON)
	
	def search_for_city(self, city_name):
		"""Input city name into search bar and click 'Search'."""
		self.city_search_input_box = city_name
		self.city_search_button.click()

		
class SearchResultsPage(BasePage):
	"""Redfin Search results page."""
	
	pass
	