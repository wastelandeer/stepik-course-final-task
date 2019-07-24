from selenium.webdriver.common.by import By

class MainPageLocators(object):
	"""docstring for MainPageLocators"""
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators(object):
	"""docstring for LoginPageLocators"""
	LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')

class ProductPageLocators(object):
	ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
	BASKET_ITEM_NAME = (By.CSS_SELECTOR, 'div.alertinner > strong')
	BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
	ITEM_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
	ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main > p')
		
