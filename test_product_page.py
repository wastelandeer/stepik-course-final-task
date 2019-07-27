from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
import pytest
import time


# @pytest.mark.parametrize('offer_num', [str(x) for x in range(10)])
# def test_guest_can_add_product_to_cart(browser, offer_num):
# #def test_guest_can_add_product_to_cart(browser):
# 	#link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# 	#link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
# 	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}'
	
# 	page = ProductPage(browser, link)
# 	page.open()
# 	# Add vars with item and price
# 	#item_name = browser.find_element_by_css_selector('div.product_main > h1').text
# 	item_name = page.get_item_name()
# 	#item_price = browser.find_element_by_css_selector('div.product_main > p').text
# 	item_price = page.get_item_price()
# 	page.add_item_to_cart()
# 	page.solve_quiz_and_get_code()
# 	#time.sleep(600)
# 	page.should_be_item_name(item_name)
# 	page.should_be_basket_total(item_price)
# 	#time.sleep(600)

# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_item_to_cart()
# 	page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_cart(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_item_to_cart()
# 	page.should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	page = ProductPage(browser, link)
	page.open()
	page.go_to_cart_page()

	cart_page = CartPage(browser, browser.current_url)
	cart_page.should_be_empty_cart_message()
	cart_page.should_not_be_product_in_cart()

class TestUserAddToCartFromProductPage(object):
	@pytest.fixture(autouse=True)
	def setup(self, browser):
		email = f'{str(time.time())}@fakemail.org'
		password = 'FYEA8ZkW77'
		link = 'http://selenium1py.pythonanywhere.com/'
		
		login_page = LoginPage(browser, link)
		login_page.open()
		login_page.go_to_login_page()
		login_page.register_new_user(email, password)
		login_page.should_be_authorized_user()
	"""Class contains tests with registered user."""
	def test_user_cant_see_success_message(self, browser):
		link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

	def test_user_can_add_product_to_cart(self, browser):
		link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
	
		page = ProductPage(browser, link)
		page.open()
	# Add vars with item and price
	#item_name = browser.find_element_by_css_selector('div.product_main > h1').text
		item_name = page.get_item_name()
	#item_price = browser.find_element_by_css_selector('div.product_main > p').text
		item_price = page.get_item_price()
		page.add_item_to_cart()
		page.solve_quiz_and_get_code()
	#time.sleep(600)
		page.should_be_item_name(item_name)
		page.should_be_basket_total(item_price)
	#time.sleep(600)
		
