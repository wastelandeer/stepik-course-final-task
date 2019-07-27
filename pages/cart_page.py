from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
	"""Class describing CartPage object with tests and merhods."""
	def should_be_empty_cart_message(self):
		assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), \
			'There should be "empty cart" message but it absent.'
	
	def should_not_be_product_in_cart(self):
		assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), \
			'There are items in cart but they should not be there.'