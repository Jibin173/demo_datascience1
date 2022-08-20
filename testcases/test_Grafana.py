import pytest
from allure_commons.types import AttachmentType

from pageobject.Dashboard import Dashboard
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageobject.DetailedReport import DetailedReport
from pageobject.AirFlow_Installation import AirFlow_Installation
from pageobject.Grafana_Installation import Grafana_Installation
from unittest import TestCase
from unittestzero import Assert
from pageobject.ClickHouseAvailibility import ClickHouseAvailibility
from selenium import webdriver
import allure

class Test_Grafana:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    grafanaurl = ReadConfig.getgrafanaurl()
    grafanadashboardurl = ReadConfig.getgrafanaurlevent()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_To_verify_that_Grafana_is_up_and_available_in_web(self, setup):
        self.logger.info("*************** Test_001 To verify that grafana is up and available in web *****************")
        self.logger.info("setup method called")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.gf = Grafana_Installation(self.driver)
        observer_title = self.gf.Grafanapagetitle()
        self.logger.debug("Observed Result of test_01_To_verify_that_Grafana_is_up_and_available_in_web is "
                          ,observer_title)
        expected_title = "Grafana"
        self.logger.debug("Expected Result for test_01_To_verify_that_Grafana_is_up_and_available_in_web is "
                          ,expected_title)
        if observer_title == expected_title:
         assert True
         print("To verify that Grafana is up and available in web:True")
         self.logger.info("To verify that Grafana is up and available in web:True")
        else:
         allure.attach(self.driver.get_screenshot_as_png(),name="To_verify_that_Grafana_is_up_and_available_in_web",
                       attachment_type=AttachmentType.PNG)
         self.logger.info("To verify that Grafana is up and available in web:False")
         assert False
        self.driver.close()

    @pytest.mark.regression
    def test_02_To_verify_that_after_providing_valid_credentials_user_is_able_to_login_the_grafana_dashboard(self,
                                                                                                             setup):
        self.logger.info("*************** Test_002_To_verify_that_after_providing_valid"
                         "_credentials_user_is_able_to_login_the_grafana_dashboard *****************")
        self.logger.info("****Started Home page title test ****")
        self.logger.info("setup method called")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.grafanaurl)
        self.gf = Grafana_Installation(self.driver)
        Observed_Result = self.gf.Login_grafana()
        self.logger.info("Observed result for To_verify_that_after_providing_valid_credentials_user_is_able_to_login_the_grafana_dashboard",
                          Observed_Result)
        Expected = True
        self.logger.info("Expected Result  for To_verify_that_after_providing_valid_credentials_user_is_able_to_login_the_grafana_dashboard ",Expected)
        assert Observed_Result == Expected
        print("To verify that after providing valid credentials user is able to login the grafana dashboard:True")
        self.logger.info("To verify that after providing valid credentials user is able to login the grafana dashboard:True")
        self.driver.close()

    @pytest.mark.regression
    def test_03_To_verify_that_summary_dashboard_should_be_available(self, setup):
        self.logger.info("*************** To_verify_that_summary_dashboard_should_be_availabl*****************")
        self.logger.info("****Started Home page title test ****")
        self.logger.debug("setup method was called")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.grafanaurl)
        self.gf = Grafana_Installation(self.driver)
        self.gf.Login_grafana()
        self.gf.table_Data()
