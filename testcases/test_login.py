import pytest
from pageobject.Dashboard import Dashboard
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageobject.DetailedReport import DetailedReport


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.dt = Dashboard(self.driver)
        actual_result = self.dt.getonline_count()
        expected_result = self.dt.databaseconnection()
        print("After running the script on grafana dashboard the value is", actual_result, "And",
              "After running the script on mysql database the value is", expected_result)
        if actual_result == expected_result:
            print("Both the script returned similar value")
        else:
            print("Both the script din't returned similar value")


    def test_to_verify_the_no_dVR_in_dashboard(self, setup):

        self.logger.info("*************** Test_003_test_to_verify_the_no_DVR_in_Dashboard*****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.dt = Dashboard(self.driver)
        self.dt.DVR_Avaialability()
