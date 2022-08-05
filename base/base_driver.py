from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:

    def __init__(self,driver):
        self.driver = driver

    # Функция для прокрутки страницы, может быть использована в любом тест кейсе.
    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Функция "wait_for_element_to_be_clickable", может быть использована в любом тест кейса.
    def wait_for_element_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element

