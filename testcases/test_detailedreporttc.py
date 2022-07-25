import pytest
from pageobject.Dashboard import Dashboard
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageobject.DetailedReport import DetailedReport


class Test002_Report:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.smoke
    def test_dash(self, setup):
         self.logger.info("****Started Home page title test ****")
         self.driver = setup
         self.logger.info("****Opening URL****")
         self.driver.get(self.baseURL)
         self.dt = DetailedReport(self.driver)
         self.dt.datetimepicker(setup)

    @pytest.mark.smoke
    def test_Featrebuttonclickable(self, setup):
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.dt = DetailedReport(self.driver)

        self.dt.button_clickable(setup)


    @pytest.mark.regression
    def test_datetime(self,setup):
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.dt = DetailedReport(self.driver)
        self.dt.date_selector(setup)








