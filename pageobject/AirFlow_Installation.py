import mysql
from selenium.webdriver.common.by import By

class AirFlow_Installation:
# WebElement
 usernametextboxxpath="//*[@id='username']"
 passwordxpathtextbox="//*[@id='password']"
 submitbutonxpath="/html/body/div[3]/div/div/div/div/div[2]/form/div[3]/div/div/input"
 Dags_in_dashbardxpath="/html/body/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/a[1]/span"
 alarm_historytextxpath="/html/body/div[3]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/strong"
 alarm_infotext_xpath="/html/body/div[3]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a/strong"
 livestatus_text_xpath="/html/body/div[3]/div/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a/strong"
 rmson_text_static_tablexpath="/html/body/div[3]/div/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/a/strong"
 version_text_xpath="/html/body/footer/div/div[1]/a"

 def __init__(self, driver):
      self.driver = driver

 def Airflowpagetitle(self):
        title=self.driver.title
        print("Title of the page",title)
        return title

 def Login_Air_Flow(self):
         usernam=self.driver.find_element_by_xpath(self.usernametextboxxpath)
         usernam.send_keys("vuelogix")
         print("Enter Username")
         password=self.driver.find_element_by_xpath(self.passwordxpathtextbox)
         password.send_keys("carinov")
         print("Entered Password")
         submit=self.driver.find_element_by_xpath(self.submitbutonxpath)
         submit.click()
         print("Submit button was clicked")
         self.driver.implicitly_wait(90)
         return self.driver.title

 def Dags_Available_(self):
     noofdags=self.driver.find_element_by_xpath(self.Dags_in_dashbardxpath)
     countofdas=int(noofdags.text)
     print("Number of dags available in the dashboard",countofdas)
     return countofdas

 def dags_verify_by_name(self):
    status1=self.driver.find_element_by_xpath(self.alarm_historytextxpath).is_displayed()
    status2=self.driver.find_element_by_xpath(self.alarm_infotext_xpath).is_displayed()
    status3=self.driver.find_element_by_xpath(self.livestatus_text_xpath).is_displayed()
    status4=self.driver.find_element_by_xpath(self.rmson_text_static_tablexpath).is_displayed()
    if status1 & status2 & status2 & status3 & status4 == True:
     return True

 def version_airflow(self):
      versio=self.driver.find_element_by_xpath(self.version_text_xpath)
      version= versio.text
      print("Observed Result",version)
      return version

