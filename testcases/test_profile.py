import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import Login_Page
from pages.sidemenu_page import SideMenu_Page
from pages.bookstore_page import BookStore_Page
from base.base_driver import BaseDriver


@pytest.mark.usefixtures("setup")
class TestProfilePage():


    #Test 1 - Check a book can be added and displayed on Profile page.
    def test_booksCanBeAddedToProfile(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()







