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
		self.driver = instance.driver
		try:
			element =  WebDriverWait(self.driver, self.wait).until(
				EC.presence_of_element_located(self.locator))
		except TimeoutException:
			raise Exception(
				f"Element could not be found using locator: {self.locator}")
		element.clear()
		element.send_keys(value)
		self.element = element

	def __get__(self, instance, owner):
		"""Retrieve this element. Return a webdriver element."""
		self.driver = instance.driver
		try:
			self.element = WebDriverWait(self.driver, self.wait).until(
				EC.presence_of_element_located(self.locator))
		except TimeoutException:
			raise Exception(
				f"Element could not be found using locator: {self.locator}")

		self._set_custom_attributes(self.element)
		return self.element

	def _set_custom_attributes(self, element):
		"""Give WebElement custom defined attributes."""
		setattr(element, "wait_for_visibility", self.wait_for_visibility)

	def wait_for_visibility(self):
		"""Wait for element to be visible in DOM."""
		return WebDriverWait(self.driver, self.wait).until(
			EC.visibility_of_element_located(self.locator))


class MultiPageElement(PageElement):
	"""Find multiple WebElements with the same locator."""

	def __get__(self, instance, owner):
		"""Retrieve elements. Return list of WebDriver elements."""
		self.driver = instance.driver
		try:
			elements = WebDriverWait(self.driver, self.wait).until(
				EC.presence_of_all_elements_located(self.locator))
		except TimeoutException:
			raise Exception(
				f"Elements could not be located with locator: {self.locator}")
		for element in elements:
			self._set_custom_attributes(element)
		self.elements = elements
		return self
