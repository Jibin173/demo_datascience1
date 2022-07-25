from selenium.webdriver.common.by import By

from pageobject.Dashboard import Dashboard


class DetailedReport:
    # WebElement
    Datetimepicker_xpath = "/html/body/div/div/main/div[3]/header/div/div[4]/div/div[1]/button[2]/div[2]/span/span[1]"
    Device_Availibility_daily_comparison_xpath = "/html/body/div/div/main/div[3]/div/div/div[1]/div/section/div/div[3]/ul/li[1]/a"
    Device_ON_OFFStatus_xpath = "/html/body/div/div/main/div[3]/div/div/div[1]/div/section/div/div[3]/ul/li[1]/a"
    Working_Summary_daily_comparison_xpath = "/html/body/div/div/main/div[3]/div/div/div[1]/div/section/div/div[3]/ul/li[1]/a"
    Date_time_picker_xpath = "/html/body/div/div/main/div[3]/header/div/div[4]/div/div[1]/button[2]"

    def __init__(self, driver):
        self.driver = driver
        print("constructor called")

    def datetimepicker(self, setup):
        DR = Dashboard(self.driver)
        print("Pointer moved to DR ")
        btn = DR.DetailedReportbutton_xpath
        self.driver.implicitly_wait(5000)
        dr = self.driver.find_element(By.XPATH, btn)
        brt = dr.is_displayed()
        print("Detailed Report button ", brt)
        dr.click()
        Device_Availibility_daily_comparison = self.driver.find_element(By.XPATH,
                                                                        self.Device_Availibility_daily_comparison_xpath)
        Device_ON_OFFStatus = self.driver.find_element(By.XPATH, self.Device_ON_OFFStatus_xpath)
        Working_Summary_daily_comparison = self.driver.find_element(By.XPATH,
                                                                    self.Working_Summary_daily_comparison_xpath)
        try:
            status1 = Device_Availibility_daily_comparison.is_displayed()
            print("Device Availibility daily comparison", status1)
        except:
            print("Device Availibility daily comparison not found")
        try:
            status2 = Device_ON_OFFStatus.is_displayed()
            print("Device_ON_OFFStatus buton", status2)
        except:
            print("Device_ON_OFFStatus button not found")
        try:
            status3 = Working_Summary_daily_comparison.is_displayed()
            print("Working_Summary_daily_comparison", status3)
        except:
            print("Working_Summary_daily_comparison button not found")

    def button_clickable(self, setup):
        DR = Dashboard(self.driver)
        print("Pointer moved to DR ")
        btn = DR.DetailedReportbutton_xpath
        self.driver.implicitly_wait(5000)
        dr = self.driver.find_element(By.XPATH, btn)
        brt = dr.is_displayed()
        print("Detailed Report button ", brt)
        dr.click()
        Device_Availibility_daily_comparison = self.driver.find_element(By.XPATH,
                                                                        self.Device_Availibility_daily_comparison_xpath)
        Device_Availibility_daily_comparison.click()

    def date_selector(self, setup):
        self.button_clickable(setup)
        self.driver.implicitly_wait(5000)

        try:
            date_time = self.driver.find_element(By.XPATH, self.Date_time_picker_xpath)
            print("Date_time enabled? ",date_time.is_displayed)
            date_time.click()
        except:
            print("Not able to find")
