#Здесь должен находиться setup метод. И Yield, который закрывает браузер после тестов.
#To run Test Cases in a particular browser,url run:
# pytest test_Login.py --browser chrome
# pytest test_Login.py --browser chrome --url https://demoqa.com/login

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup(request,browser): #,url Добавить в скобки если хочу запустить с другим url.
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser.")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox browser.")
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser.")
    driver.implicitly_wait(5)
    driver.get("https://demoqa.com/login")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    print("Closing Chrome browser")
    driver.close()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--url")

@pytest.fixture()   #Запускать с определённого браузера.
def browser(request):
    return request.config.getoption("--browser")

# @pytest.fixture()   #Запускать с определённым url.
# def url(request):
#     return request.config.getoption("--url")