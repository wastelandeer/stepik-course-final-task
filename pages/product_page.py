from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	"""ProductPage class to test adding item to cart."""
	def get_item_name(self):
		if not self.is_element_present(*ProductPageLocators.ITEM_NAME):
			return None
		return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
	
	def get_item_price(self):
		if not self.is_element_present(*ProductPageLocators.ITEM_PRICE):
			return None
		return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
	
	def add_item_to_cart(self):
		self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

	def should_be_item_name(self, item):
		item_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME).text
		#item_in_basket = '123'
		assert item == item_in_basket, f'Items names mismatch. Name on item page: {item}, name in basket: {item_in_basket}.'
	
	def should_be_basket_total(self, price):
		basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
		#basket_total = '456'
		assert price == basket_total, f'Prices mismatch. Item price: {price}, basket total price: {basket_total}.'

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.BASKET_ITEM_NAME),\
			'Success message is presented, but should not be.'

	def should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.BASKET_ITEM_NAME),\
			'Success message didn`t disappear, but it should.'