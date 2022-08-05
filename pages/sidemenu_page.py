from selenium.webdriver.common.by import By

class SideMenu_Page:


    def __init__(self, driver):
        self.driver = driver


    # Locators.
    button_BookStore_xpath = "//div[@class='left-pannel'] /div/div[6]/div/ul/li[2]"
    button_Profile_xpath = "//div[@class='element-list collapse show']//li[@id='item-3']"


    # Action methods.
    def clickButtonBookStore(self):
        book_store = self.driver.find_element(By.XPATH, self.button_BookStore_xpath)
        self.driver.execute_script("arguments[0].click();", book_store)

    def clickButtonProfile(self):
        profile = self.driver.find_element(By.XPATH, self.button_Profile_xpath)
        self.driver.execute_script("arguments[0].click();", profile)