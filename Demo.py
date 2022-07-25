from psutil import users
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\josej\\Downloads\\chromedriver_win32(1)\chromedriver.exe")

##TestCase 1

print("TC.1 To verify the title is correct or not")
driver.get("http://3.108.221.40:8080/v-protect")
Expectedtile = "Login"
Actualresult = driver.title
print("Actual Result is", Actualresult, "Expected Result is", Expectedtile)
assert Expectedtile in Actualresult
driver.close()

print(
    "***************************************************************************************************************************")

##TestCase 2

driver = webdriver.Chrome(executable_path="C:\\Users\\josej\\Downloads\\chromedriver_win32(1)\chromedriver.exe")
print("TC.2: To verify the status of database")
driver.get("http://3.108.221.40:8080/v-protect")
driver.maximize_window()
availability = False
driver.implicitly_wait(5000)
element = driver.find_element(By.XPATH, '/html/body/div[1]/ul/li[2]/a')
availability = element.is_displayed()
print("Button is", availability)
driver.implicitly_wait(5000)
print("Implicit wait used and now executing further statements")
element.click()
driver.implicitly_wait(5000)
try:
    verify = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td[1]')
    descion = verify.is_displayed
    print("Script identified the satus?", descion)
    status = driver.find_element(By.XPATH, '//*[@id="FernoAccess"]')
    print("Your database availibilty", status.text)
    assert "SUCCESS" in status.text
    driver.close()

except:
    print("Not able to execute the database status")
    driver.close()

print(
    "*******************************************************************************************************************")

##TestCase 3

print("TC_3: To verify that user is able to login the application")
driver = webdriver.Chrome(executable_path="C:\\Users\\josej\\Downloads\\chromedriver_win32(1)\chromedriver.exe")
driver.get("http://3.108.221.40:8080/v-protect")
driver.maximize_window()
try:
    driver.implicitly_wait(5000)
    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    print("Username textbox is available??", username.is_displayed)
    username.send_keys("admin")
except:
    print("Username textbox is available??", username.is_displayed)
    driver.close()
try:
    driver.implicitly_wait(5000)
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    print("Password textbox is available?", password.is_displayed)
    password.send_keys("carinov@123")
except:
    print("password text box is available?", password.is_displayed)
    driver.close()
try:
    driver.implicitly_wait(5000)
    submitbutton = driver.find_element(By.XPATH, '/html/body/div[3]/form/div[4]/button')
    print("Submit button available?", submitbutton.is_displayed)
    submitbutton.click()
except:
    print("not able to click the submit button")
