from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///Users/vijaysharma/Desktop/registration_project/index.html")

time.sleep(2)

driver.find_element(By.ID,"fname").send_keys("Vijay")
time.sleep(1)

driver.find_element(By.ID,"lname").send_keys("Sharma")
time.sleep(1)

driver.find_element(By.ID,"email").send_keys("Vijaysharma@gmail.com")
time.sleep(1)

driver.find_element(By.ID,"phone").send_keys("9999999999")
time.sleep(1)

driver.find_element(By.ID,"age").send_keys("21")
time.sleep(1)

driver.find_element(By.ID,"male").click()
time.sleep(1)

driver.find_element(By.ID,"address").send_keys("Ahmedabad, Gujarat")
time.sleep(1)

driver.find_element(By.ID,"password").send_keys("StrongPass123")
time.sleep(1)

driver.find_element(By.ID,"confirm").send_keys("StrongPass123")
time.sleep(1)

driver.find_element(By.ID,"terms").click()
time.sleep(1)

driver.find_element(By.TAG_NAME,"button").click()

time.sleep(4)

print("Registration Successful Page Loaded")

driver.quit()
