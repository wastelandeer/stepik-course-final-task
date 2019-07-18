import pytest
from selenium import webdriver

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default='en',
		help='Specify user language for tests')

@pytest.fixture()
def browser(request):
	options = webdriver.ChromeOptions()
	options.add_experimental_option('w3c', False)
	
	browser_language = request.config.getoption('language')
	options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
	
	browser = webdriver.Chrome(options=options)
	yield browser
	browser.quit()