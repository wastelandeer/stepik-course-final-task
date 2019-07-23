from selenium.webdriver.common.by import By

class MainPageLocators(object):
	"""docstring for MainPageLocators"""
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators(object):
	"""docstring for LoginPageLocators"""
	LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
