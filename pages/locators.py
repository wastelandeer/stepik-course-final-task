from selenium.webdriver.common.by import By

# class MainPageLocators(object):
# 	"""docstring for MainPageLocators"""
# 	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators(object):
	"""docstring for LoginPageLocators"""
	LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
	REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
	REGISTER_FORM_PASS1 = (By.CSS_SELECTOR, 'input#id_registration-password1')
	REGISTER_FORM_PASS2 = (By.CSS_SELECTOR, 'input#id_registration-password2')
	REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators(object):
	ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
	BASKET_ITEM_NAME = (By.CSS_SELECTOR, 'div.alertinner > strong')
	BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
	ITEM_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
	ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main > p')
	#SUCCESS_MESSAGE = (By.CSS_SELECTOR, '')

class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
	CART_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn-default')
	USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class CartPageLocators(object):
	EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div.content > div#content_inner > p')
	CART_ITEMS = (By.CSS_SELECTOR, 'div.content > div#content_inner > div')
		
				
