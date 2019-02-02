"""Base classes for test objects."""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
	"""Base page for initialization.

	Enables usage of PageElement.
	"""

	def __init__(self, driver):
		"""Initialize with current driver."""
		self.driver = driver


class PageElement(object):
	"""A generic page element.

	Contains overwritten get and set methods for ease of use.
	"""

	def __init__(self, locator, wait=10):
		"""Initialize this element.

		args:
			wait: int; time to wait for this element, in seconds.
			locator: tuple; locator strategy and string used to find element.
		"""
		self.locator = locator
		self.wait = wait
		self.element = None

	def __set__(self, instance, value):
		driver = instance.driver
		try:
			element =  WebDriverWait(driver, self.wait).until(
				EC.presence_of_element_located(self.locator))
		except TimeoutException:
			raise Exception(
				f"Element could not be found using locator: {self.locator}")
		element.clear()
		element.send_keys(value)
		self.element = element

	def __get__(self, instance, owner):
		"""Retrieve this element. Return a webdriver element."""
		driver = instance.driver
		try:
			self.element = WebDriverWait(driver, self.wait).until(
				EC.presence_of_element_located(self.locator))
		except TimeoutException:
			raise Exception(
				f"Element could not be found using locator: {self.locator}")

		return self.element
