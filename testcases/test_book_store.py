import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import Login_Page
from pages.sidemenu_page import SideMenu_Page
from pages.bookstore_page import BookStore_Page
from base.base_driver import BaseDriver


@pytest.mark.usefixtures("setup")
class TestBookStorePage():

    #Assertions.

    #5. Add a book to your collection and verify that it's present on the Profile page.
    #6. Verify that there is a Delete button on the Profile page.
    #7. Verify that there is a Go To Book Store button on the Profile page.
    # Click it, and verify that Book Store page is opened.

    #Test 1 - Search box is present on the Book Store page.
    def test_searchbox_present(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH,"//button[@id='login']").click()

        #Open Book Store page.
        page_submenu.clickButtonBookStore()
        #base_driver.page_scroll()
        print(page_bookstore.searchbox())

        #Assertion. The Search bar is present.
        if page_bookstore.searchbox() == True:
            print("PASSED - The Search box is displayed.")
            assert True
        else:
            print("FAILED - The Search box is not displayed.")
            assert False


    #Test 2 - Check that there are 4 headers in the table.
    def test_tableHeaderConsistsOfElements(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()

        #Open Book Store page.
        page_submenu.clickButtonBookStore()

        #Assertion. Check that all Headers are in the table header.
        if page_bookstore.ImageTableHeader() == "Image" and page_bookstore.TitleTableHeader() == "Title"\
                and page_bookstore.AuthorTableHeader() == "Author" and page_bookstore.PublisherTableHeader() == "Publisher":
            print("PASSED - All 4 Headers are present.")
            assert True
        else:
            print("FAILED - Some of the Headers are missing.")
            assert False


    #Test 3 - Check that there is a logout button.
    def test_logoutButtonPresent(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(3)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()

        #Assertion. Check that there is a logout button.
        if page_bookstore.LogoutButtonIsDisplayed() == True:
            print("PASSED - The Logout button is displayed.")
            assert True
        else:
            print("FAILED - The Logout button is missing.")
            assert False


    #Test 4 - Check that the table by default consists of 10 rows.
    def test_tableConsistsOfRows(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()

        #Assertion. Check that the table by defaul consists of 10 rows.
        if int(page_bookstore.TableRowsByDefault()) == 10:
            print("PASSED - There are 10 rows by default.")
            assert True
        else:
            print("FAILED - There aren't 10 rows by default.")
            assert False


    #Test 5 - Check that there are 8 books.
    def test_numberOfBooksByDefault(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()

        #Assertion - Check that there are 8 books.
        if page_bookstore.TableNumberOfDefaultBooks() == 8:
            print("PASSED - There are 8 books by default.")
            assert True
        else:
            print("FAILED - There are 8 books by default.")
            assert False


    #Test 6 - Check books by their Publisher.
    def test_numberOfBooksByPublisher(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()

        #Assertion - Check books by their Publisher.
        if page_bookstore.TableNumberOfBooksByPublisher() == 6:
            print("PASSED - There are 6 books by a particular publisher.")
            assert True
        else:
            print("FAILED - There aren't 6 books by a partucular publisher.")
            assert False


    #Test 7 - The Page Info is present.
    def test_pageInfoPresent(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()
        #Assertion - The Page Info is present.
        if page_bookstore.PageInfoPresent() == "Page of 1":
            print("PASSED - The page info is present.")
            assert True
        else:
            print("FAILED - The page info is missing.")
            assert False


    #Test 8 - Check that Search results are present and the book if displayed in the table.
    def test_seachResultsDisplayedInTable(self):
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()

        #Assertion - Check that Search results are present and the book if displayed in the table.
        if page_bookstore.RandomSearchResults() == page_bookstore.ValidateRandomSearchResults():
            print("PASSED - The book is displayed in the table.")
            assert True
        else:
            print("FAILED - The book is not displayed in the table.")
            assert False


    # Test 9 - Get random book from a list of books and compare it with a table, then click on a link.
    # def test_OpenBookDetailsByChoosingRandomBookFromTable(self):
    #     #Objects of pages.
    #     page_login = Login_Page(self.driver)
    #     page_bookstore = BookStore_Page(self.driver)
    #     page_submenu = SideMenu_Page(self.driver)
    #     base_driver = BaseDriver(self.driver)
    #
    #     #Logging in the app.
    #     page_login.enterUsername("TestUserName")
    #     page_login.enterPassword("123QWEasdZXC!")
    #     base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
    #     time.sleep(1)
    #
    #     #Open Book Store page.
    #     page_submenu.clickButtonBookStore()
    #
    #     #Get random book and compare it with a table.
    #     page_bookstore.GetRandomBookAndCompareWithTable()


    def test_VerifyTitleAuthor(self):
        #Test 9 - Get a book from a table and verify that Title and Author is the same as in the table.
        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()
        page_bookstore.Title()
        page_bookstore.Author()
        page_bookstore.clickAuthor()

        #Assertion - Get a book from a table and verify that Title and Author is the same as in the table.
        if page_bookstore.VerifyTitle() == "Git Pocket Guide" and page_bookstore.VerifyAuthor() == "Richard E. Silverman":
            print("PASSED - The Title and Author of the book matches.")
            assert True
        else:
            print("FAILED - The Title and Author of the book doesn't match.")
            assert False


    #Test 10 - Verify the "Back To Book Store" is on the page and clickable.
    def test_VerifyBackToStoreButton(self):

        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()
        page_bookstore.clickAuthor()

        #Assertion - Verify the "Back To Book Store" is on the page and is clickable or enabled.
        if page_bookstore.IsEnabledBackToStore() == True:
            print("PASSED - The Back_To_Book_Store button is enabled.")
            assert True
        else:
            print("FAILED - The Back_To_Book_Store button is not enabled.")
            assert False


    #Test 11 - Verify that "Book Store" with search bar is displayed.
    def test_VerifyBackToStoreButtonIsClickedAndBookStoreIsDisplayed(self):

        #Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        #Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        #Open Book Store page.
        page_submenu.clickButtonBookStore()
        page_bookstore.clickAuthor()
        page_bookstore.clickBackToStore()

        #Assertion - Verify that "Book Store" with search bar is displayed.
        if page_bookstore.searchbox() == True:
            print("PASSED - The Button is clicked, the Book Store is displayed.")
            assert True
        else:
            print("FAILED - The Button is not clicked, the Book Store is not displayed.")
            assert False


    # Test 12 - Click the "Add To Your Collection" button and verify that
    # the Alert pop-up is present and "User is authorized!" is displayed.
    def test_VerifyAlertIsDisplayed(self):

        # Objects of pages.
        page_login = Login_Page(self.driver)
        page_bookstore = BookStore_Page(self.driver)
        page_submenu = SideMenu_Page(self.driver)
        base_driver = BaseDriver(self.driver)

        # Logging in the app.
        page_login.enterUsername("TestUserName")
        page_login.enterPassword("123QWEasdZXC!")
        base_driver.wait_for_element_to_be_clickable(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)

        # Open Book Store page.
        page_submenu.clickButtonBookStore()
        page_bookstore.clickAuthor()
        page_bookstore.clickAddToYourCollection()
        time.sleep(1)

        #Assertion - Click the "Add To Your Collection" button and verify that
        # the Alert pop-up is present and "User is authorized!" is displayed.
        if page_bookstore.verifyAllert() == "Book added to your collection." or "Book already present in the your collection!":
            print("PASSED - The Alert is displayed, the text is present.")
            assert True
        else:
            print("FAILED - The Alert is not displayed, the text is not present.")
            assert False





