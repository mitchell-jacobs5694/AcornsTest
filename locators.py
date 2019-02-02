from selenium.webdriver.common.by import By


class HomePageLocators:
	"""Class for Home Page locators."""

	CITY_SEARCH_INPUT = (By.XPATH, "//div[@id='homepageTabContainer']//input[@id='search-box-input']")
	CITY_SEARCH_BUTTON = (By.XPATH,  "//div[@id='homepageTabContainer']//button[@title='Search']")


class SearchResultsPageLocators:
	"""Class for search result page locators."""

	APPLY_FILTERS = (By.XPATH, "//button[@data-rf-test-id='apply-search-options']")
	MAX_BEDS = (By.XPATH, "//select[@name='maxBeds']")
	MAX_FEET = (By.XPATH, "//select[@name='sqftMax']")
	MAX_PRICE = (By.XPATH, "//select[@name='maxPrice']")
	MIN_BEDS = (By.XPATH, "//select[@name='minBeds']")
	MIN_FEET = (By.XPATH, "//select[@name='sqftMin']")
	MIN_PRICE = (By.XPATH, "//select[@name='minPrice']")
	MORE_FILTERS= (By.XPATH, "//button[@data-rf-test-id='filterButton']")
	RESULT_ADDRESS = (By.XPATH, "//td[@class='column column_1 col_address']//a")
	RESULT_BATHS = (By.XPATH, "//td[@class='column column_5 col_baths']")
	RESULT_BEDS = (By.XPATH, "//td[@class='column column_4 col_beds']")
	RESULT_SQ_FEET = (By.XPATH, "//td[@class='column column_6 col_sqft']")
	RESULT_PRICE = (By.XPATH, "//td[@class='column column_3 col_price']")
	RESULTS_LIST = (By.XPATH, "//tbody[@class='tableList']//tr")
	RESULTS_TABLE = (By.XPATH, "//span[@data-rf-test-name='tableOption']")
