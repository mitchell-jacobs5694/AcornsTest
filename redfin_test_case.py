import unittest
from selenium import webdriver
from pages.redfin_pages import HomePage
import time

class RedfinSearchTestCase(unittest.TestCase):
	"""Search Redfin and verify correct search results."""
	
	def setUp(self):
		"""Set up driver before test begins."""
		
		# make work with all drivers?
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.redfin.com")

	def test_property_search_with_filters(self):
		"""Search using filters and verify search results."""
		homepage = HomePage(self.driver)
		homepage.search_for_city("Gardena")
		time.sleep(3)
	
	def tearDown(self):
		"""Quit driver instance."""
		self.driver.quit()



if __name__ == "__main__":
	# add CLI arg using arg parse to specify browser?
	# need all browser drivers?
	
	#can pass cl args to below .main(argv = args)
	unittest.main()