import random
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class BookStore_Page(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)    #Передаю всю строку с super() чтобы взять класс с "base_driver" где у меня функция скролл и теперь scroll функцию можно вызывать как отсюда, так и с base_driver.
        self.driver = driver        #Это берётся с "conftest" и передаётся сюда и в init метод чтобы заработал драйвер.


    #Locators.
    SearchBox_xpath = "//input[@id='searchBox']"
    table_header_xpath = "//div[@class='rt-tr']/div/div[@class='rt-resizable-header-content']"
    logout_btn_xpath = "//button[@id='submit']"
    pageInfo_xpath = "//span[@class='-pageInfo']"
    table_image_xpath = "//div[(text()='Image')]"
    table_title_xpath = "//div[(text()='Title')]"
    table_author_xpath = "//div[(text()='Author')]"
    table_publisher_xpath = "//div[(text()='Publisher')]"
    table_rows_xpath = "//div[@class='rt-tbody']/div"
    title_xpath = "//a[normalize-space()='Git Pocket Guide']"
    author_xpath = "//div[normalize-space()='Richard E. Silverman']"
    link_title_xpath = "//a[normalize-space()='Git Pocket Guide']"
    book_details_title_xpath = "//div[@id='title-wrapper']//label[@id='userName-value']"
    book_details_author_xpath = "//div[@id='author-wrapper']//label[@id='userName-value']"
    btn_BackToStore_xpath = "//div[@class='text-left fullButton']//button[@id='addNewRecordButton']"
    btn_AddToYourCollection_xpath = "//div[@class='text-right fullButton']//button[@id='addNewRecordButton']"

    #Action methods.
    def searchbox(self):
        searchbox_element = self.driver.find_element(By.XPATH, self.SearchBox_xpath).is_displayed()
        return searchbox_element

    def ImageTableHeader(self):
        image = self.driver.find_element(By.XPATH, self.table_image_xpath).text
        return image


    #Headers of the table.
    def TitleTableHeader(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        return title

    def AuthorTableHeader(self):
        author = self.driver.find_element(By.XPATH, self.table_author_xpath).text
        return author

    def PublisherTableHeader(self):
        publisher = self.driver.find_element(By.XPATH, self.table_publisher_xpath).text
        return publisher
    #--------------------------------------------


    def LogoutButtonIsDisplayed(self):
        logout_button = self.driver.find_element(By.XPATH, self.logout_btn_xpath).is_displayed()
        return logout_button

    def TableRowsByDefault(self):
        table_rows = len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))
        return int(table_rows)

    def TableNumberOfDefaultBooks(self):
        rows_in_table = self.driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']/div/div/div")
        books_count = 0
        for r in range(1, len(rows_in_table) + 1, +1):
            title = self.driver.find_element(By.XPATH,"//div[@class='rt-tbody']/div[" + str(r) + "]/div/div[2]/div/span").text
            books_count = books_count + 1
            print(title)
        return books_count

    def TableNumberOfBooksByPublisher(self):
        rows_in_table = self.driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']/div/div/div")
        print(len(rows_in_table))
        count_publisher = 0
        for r in range(1, len(rows_in_table) + 1, +1):
            publisher = self.driver.find_element(By.XPATH, "//div[@class='rt-tbody'] /div["+str(r)+"]/div/div[4]").text
            if publisher == "O'Reilly Media":
                count_publisher = count_publisher + 1
                print(count_publisher)
                print(publisher)
        return count_publisher

    def PageInfoPresent(self):
        page_info = self.driver.find_element(By.XPATH, self.pageInfo_xpath).text
        print(page_info)
        return page_info


    #Search feature.
    def RandomSearchResults(self):      #Get random search results.
        list_of_books = ["Git Pocket Guide", "Learning JavaScript Design Patterns",
                         "Designing Evolvable Web APIs with ASP.NET", "Speaking JavaScript",
                         "You Don't Know JS", "Programming JavaScript Applications",
                         "Eloquent JavaScript, Second Edition", "Understanding ECMAScript 6"]

        self.driver.find_element(By.XPATH, "//input[@id='searchBox']").send_keys(random.choice(list_of_books))
        search_box_get_value = self.driver.find_element(By.XPATH, "//input[@id='searchBox']").get_attribute("value")
        print(search_box_get_value)
        return search_box_get_value

    def ValidateRandomSearchResults(self):      #Compare random search results with the table.
        table_rows = self.driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div")
        for r in range(1, len(table_rows) + 1, +1):
            title = self.driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div["+str(r)+"]/div/div[2]").text
            print(title)
            return title


    def GetRandomBook(self):        #Get a random book from a list.
        list_of_books = ["Git Pocket Guide", "Learning JavaScript Design Patterns",
                         "Designing Evolvable Web APIs with ASP.NET", "Speaking JavaScript",
                         "You Don't Know JS", "Programming JavaScript Applications",
                         "Eloquent JavaScript, Second Edition", "Understanding ECMAScript 6"]
        random_book = random.choice(list_of_books)
        print(random_book)
        return random_book


    def GetRandomBookAndCompareWithTable(self):    #Get random book and compare it with a table.
        list_of_books = ["Git Pocket Guide", "Learning JavaScript Design Patterns",
                         "Designing Evolvable Web APIs with ASP.NET", "Speaking JavaScript",
                         "You Don't Know JS", "Programming JavaScript Applications",
                         "Eloquent JavaScript, Second Edition", "Understanding ECMAScript 6"]
        random_book = random.choice(list_of_books)
        print(random_book)

        while True:
            table_rows = self.driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div")
            for r in range(1, len(table_rows) + 1, +1):
                title = self.driver.find_element(By.XPATH,"//div[@class='rt-tbody']/div[" + str(r) + "]/div/div[2]/div/span/a").text
                print(title)
                if random_book == title:
                    print("Found: ", random_book, title)
                    self.driver.find_element(By.XPATH,"//div[@class='rt-tbody']/div[" + str(r) + "]/div/div[2]/div/span").click()
                # else:
                #     print("The is no book matching the value.")
            break
        return random_book

    def Title(self):
        title = self.driver.find_element(By.XPATH, self.title_xpath).text
        return title

    def Author(self):
        author = self.driver.find_element(By.XPATH, self.author_xpath).text
        return author

    def clickAuthor(self):
        self.driver.find_element(By.XPATH, self.link_title_xpath).click()

    def VerifyTitle(self):
        verify_title = self.driver.find_element(By.XPATH, self.book_details_title_xpath).text
        return verify_title

    def VerifyAuthor(self):
        verify_author = self.driver.find_element(By.XPATH, self.book_details_author_xpath).text
        return verify_author

    def IsEnabledBackToStore(self):
        btn_back_to_store = self.driver.find_element(By.XPATH, self.btn_BackToStore_xpath).is_enabled()
        return btn_back_to_store

    def clickBackToStore(self):
        self.driver.find_element(By.XPATH, self.btn_BackToStore_xpath).click()

    def clickAddToYourCollection(self):
        self.driver.find_element(By.XPATH, self.btn_AddToYourCollection_xpath).click()

    def verifyAllert(self):
        alert_text = self.driver.switch_to.alert.text
        print(alert_text)
        self.driver.switch_to.alert.accept()
        return alert_text