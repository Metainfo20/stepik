import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

languages = ["ar","ca","cs","da","de","en-gb","el","es","fi","fr","it","ko","nl","pl","pt","pt-br","ro","ru","sk","uk","zh-hans"]

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

def pytest_language_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help=f"Supporting languages: {languages}")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language in languages:
        print(f"\nstart chrome browser for test in {language}..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError(f"--language should be: {languages}")
    yield browser
    print("\nquit browser..")
    browser.quit()
