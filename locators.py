from selenium.webdriver.common.by import By


class HomePageLocators:
	"""Class for Home Page locators."""
	
	CITY_SEARCH_INPUT = (By.XPATH, "//div[@id='homepageTabContainer']//input[@id='search-box-input']")
	CITY_SEARCH_BUTTON = (By.XPATH,  "//div[@id='homepageTabContainer']//button[@title='Search']")