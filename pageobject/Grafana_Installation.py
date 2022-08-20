from Utilities.customLogger import LogGen


class Grafana_Installation:
    logger = LogGen.loggen()
    # WebElement
    Grafanausername_xpath = "/html/body/div/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input"
    Grafanapassword_xpath = "//*[@id='current-password']"
    Grafanasubmit_xpath = "/html/body/div/div/main/div[3]/div/div[2]/div/div/form/button"
    Grafana_EventSummarydashboard = "//*[@id='reactRoot']/div/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/section/div[1]/header/div/h2"
    Grafana_No_data = "/html/body/div/div/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/section/div[2]/div/p"

    def __init__(self, driver):
        self.driver = driver

    def Grafanapagetitle(self):
        self.logger.info("Grafanapagetitle method was called")
        title = self.driver.title
        print("Title of the page", title)
        self.logger.debug("returning the title of the page as",title)
        return title

    def Login_grafana(self):
        username = self.driver.find_element_by_xpath(self.Grafanausername_xpath)
        username.send_keys("vuelogix")
        password = self.driver.find_element_by_xpath(self.Grafanapassword_xpath)
        password.send_keys("carinov")
        submitbtn = self.driver.find_element_by_xpath(self.Grafanasubmit_xpath)
        self.driver.implicitly_wait(890)
        submitbtn.click()
        dasboardavailable = self.driver.find_element_by_xpath(self.Grafana_EventSummarydashboard)
        status = dasboardavailable.is_displayed()
        return status

    def table_Data(self):
        status = self.driver.find_element_by_xpath(self.Grafana_No_data)
        rtstatus = status.is_displayed()
        print(rtstatus)
        assert rtstatus == False
