import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demoqa.com/")
driver.implicitly_wait(5)
actions = ActionChains(driver)


book_store_item = driver.find_element(By.XPATH,"//div[@class='home-content'] /div[2]/div/div[6]")
driver.execute_script("arguments[0].click();", book_store_item)
login = driver.find_element(By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-0']")
driver.execute_script("arguments[0].click();", login)
book_store = driver.find_element(By.XPATH,"//div[@class='left-pannel'] /div/div[6]/div/ul/li[2]")
driver.execute_script("arguments[0].click();", book_store)

driver.find_element(By.XPATH,"//button[@id='login']").click()
username_textbox = driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("TestUserName")
password_textbox = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("123QWEasdZXC!")
driver.find_element(By.XPATH,"//button[@id='login']")




list_of_books = ["Git Pocket Guide", "Learning JavaScript Design Patterns",
                 "Designing Evolvable Web APIs with ASP.NET", "Speaking JavaScript",
                 "You Don't Know JS", "Programming JavaScript Applications",
                 "Eloquent JavaScript, Second Edition", "Understanding ECMAScript 6"]
random_book = random.choice(list_of_books)
print(random_book)

while True:
    table_rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div")
    for r in range(1, len(table_rows) + 1, +1):
        title = driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div[" + str(r) + "]/div/div[2]/div/span/a").text
        print(title)
        if random_book == title:
            print("Found: ", random_book, title)
            driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div[" + str(r) + "]/div/div[2]/div/span").click()
        else:
            print("The is no book matching the value.")
    break


time.sleep(1)
driver.close()
