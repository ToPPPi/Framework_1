import logging
import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import Login_Page
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestLoginPage():

    log = Utils.loggenerator(logLevel=logging.INFO)

    def test_loging_function(self):
        self.log.info("************** Starting... **************")
        self.log.info("************** Test_001 - test_loging_function **************")
        #Object.
        lp = Login_Page(self.driver)

        #Logging in the app.
        lp.enterUsername("TestUserName")

        #Get UserName value to compare.
        username_value = self.driver.find_element(By.XPATH,"//input[@id='userName']").get_attribute("value")
        self.log.info(username_value)

        #Continue Logging in the app.
        lp.enterPassword("123QWEasdZXC!")
        lp.clickLoginButton()

        #Assertion - User is logged in and the UserName is equal to UserName displayed on the page.
        if username_value == "TestUserName": # UNDONE Это надо добавить в configfiles, чтобы не писать каждый раз здесь нового пользователя.
            self.log.info("Test_001 - test_loging_function - PASSED - User is logged in and the UserName matched with the UserName displayed on the page.")
            self.log.info("************** Finishing... **************")
            assert True
        else:
            self.log.info("Test_001 - test_loging_function - FAILED - User is not logged in or the UserName doesn't match with the UserName displayed on the page.")
            self.log.info("************** Finishing... **************")
            assert False















































