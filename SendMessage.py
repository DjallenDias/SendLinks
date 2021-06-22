from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class TypeWords:
	def __init__(self, driver):
		self.driver = driver

	def type(self, message):
		self.driver.find_element_by_css_selector("span[title='']").click()
		self.entry = self.driver.find_elements_by_css_selector("div[class='_2_1wd copyable-text selectable-text']")
		self.teclas = Keys.SHIFT + Keys.ENTER + Keys.SHIFT
		self.message = message.replace("\n", self.teclas)
		self.entry[1].send_keys(self.message, Keys.ENTER)
