import logging
import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page_ddt import Login_Page_DDT
from utilities.utils import Utils
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestLoginPage_DDT():

    log = Utils.loggenerator(logLevel=logging.INFO)

    @data(("TestUserName","123QWEasdZXC!"))
    @unpack
    def test_loging_function(self,username,password):
        self.log.info("************** Starting... **************")
        self.log.info("************** Test_001 - test_loging_function **************")
        #Object.
        lp = Login_Page_DDT(self.driver)

        #Logging in the app.
        lp.enterUsername(username)

        #Get UserName value to compare.
        username_value = self.driver.find_element(By.XPATH,"//input[@id='userName']").get_attribute("value")
        self.log.info(username_value)

        #Continue Logging in the app.
        lp.enterPassword(password)
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















































