from selenium.webdriver.common.by import By


class HomePageLocators:
	"""Class for Home Page locators."""

	CITY_SEARCH_INPUT = (By.XPATH, "//div[@id='homepageTabContainer']//input[@id='search-box-input']")
	CITY_SEARCH_BUTTON = (By.XPATH,  "//div[@id='homepageTabContainer']//button[@title='Search']")


class SearchResultsPageLocators:
	"""Class for search result page locators."""

	MAX_BEDS = (By.XPATH, "//select[@name='maxBeds']")
	MAX_PRICE = (By.XPATH, "//select[@name='maxPrice']")
	MIN_BEDS = (By.XPATH, "//select[@name='minBeds']")
	MIN_PRICE = (By.XPATH, "//select[@name='minPrice']")
	MORE_FILTERS= (By.XPATH, "//button[@data-rf-test-id='filterButton']")
