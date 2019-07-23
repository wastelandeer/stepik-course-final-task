from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #link ='http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    link = 'http://selenium1py.pythonanywhere.com/'
    
    #page = MainPage(browser, link)
    #page.open()
    #page.go_to_login_page()
    #page.should_be_login_link()

    login_page = LoginPage(browser, link)
    login_page.open()
    #login_page.should_be_login_url()
    #login_page.should_be_login_form()
    #login_page.should_be_register_form()
