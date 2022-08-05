from selenium.webdriver.common.by import By

class Login_Page:

    def __init__(self,driver):
        self.driver = driver


    #Locators.
    button_Login_xpath = "//button[@id='login']"
    textfield_username_xpath = "//input[@id='userName']"
    textfield_password_xpath = "//input[@id='password']"

    #Action methods.
    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def enterUsername(self,username):
        self.driver.find_element(By.XPATH, self.textfield_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textfield_username_xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.textfield_username_xpath)
        self.driver.find_element(By.XPATH, self.textfield_password_xpath).send_keys(password)