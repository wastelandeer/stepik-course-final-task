from pages.product_page import ProductPage
import pytest
#import time


@pytest.mark.parametrize('offer_num', [str(x) for x in range(10)])
def test_guest_can_add_product_to_cart(browser, offer_num):
	#link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
	#link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}'
	
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