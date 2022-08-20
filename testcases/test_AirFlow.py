from configparser import NoOptionError

import pytest
from pageobject.Dashboard import Dashboard
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageobject.DetailedReport import DetailedReport
from pageobject.AirFlow_Installation import AirFlow_Installation


class Test_AirFlow:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    airflowURL = ReadConfig.getairflow()

    @pytest.mark.regression
    def test_04_To_verify_that_the_Airflow_is_available_on_Web(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.logger.warning("execution")
        self.driver.get(self.airflowURL)
        self.ar = AirFlow_Installation(self.driver)
        observer_title = self.ar.Airflowpagetitle()
        expected_title = "Sign In - Airflow"
        assert observer_title == expected_title
        print("test_01_To_verify_that_the_Airflow_is_available_on_Web:True")
        self.driver.close()

    @pytest.mark.regression
    def test_05_To_verify_that_user_is_able_to_login_the_Airflow_application_with_valid_credentials(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.airflowURL)
        self.ar = AirFlow_Installation(self.driver)
        observed_title = self.ar.Login_Air_Flow()
        assert observed_title == "DAGs - Airflow"
        countdages = self.ar.Dags_Available_()
        assert countdages == 4
        print("To_verify_that_user_is_able_to_login_the_Airflow_application_with_valid_credentials:True")
        self.driver.close()

    @pytest.mark.regression
    def test_06_To_verify_that_required_dags_are_available_in_the_dashboard(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.airflowURL)
        self.ar = AirFlow_Installation(self.driver)
        self.ar.Login_Air_Flow()
        observedresult = self.ar.dags_verify_by_name()
        assert observedresult == True
        print("To verify that required dags are available in the dashboard: True")
        self.driver.close()

    @pytest.mark.regression
    def test_07_To_verify_the_version_of_the_Airflow(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.airflowURL)
        self.ar = AirFlow_Installation(self.driver)
        self.ar.Login_Air_Flow()
        observed = self.ar.version_airflow()
        exversion = 'v2.2.0'
        assert observed == exversion
        print("To verify the version of the Airflow: True")
        self.driver.close()
