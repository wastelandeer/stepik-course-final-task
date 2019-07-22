from .basepage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
	"""docstring for MainPage"""
	
	def go_to_login_page(self):
    link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    link.click()
