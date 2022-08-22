import pytest
from pageobject.Dashboard import Dashboard
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageobject.DetailedReport import DetailedReport
from pageobject.AirFlow_Installation import AirFlow_Installation
from pageobject.Grafana_Installation import Grafana_Installation
from unittest import TestCase
from unittestzero import Assert
from pageobject.ClickHouseAvailibility import  ClickHouseAvailibility


class Test_Clickhouse:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    grafanaurl = ReadConfig.getgrafanaurl()
    grafanadashboardurl = ReadConfig.getgrafanaurlevent()

    @pytest.mark.regression
    def test_08_To_verify_that_connection_towards_clickhouse_is_available(self, setup):
        self.logger.info("*************** Test_001_To verify that connection towards clickhouse is available *****************")
        self.driver = setup
        self.ck = ClickHouseAvailibility(self.driver)
        self.ck.databaseactivity()
        self.driver.close()

    @pytest.mark.regression
    def test_09_To_verify_that_required_Schema_is_available(self,setup):
        self.logger.info("*************** Test_001_To verify that connection towards clickhouse is available *****************")
        self.driver = setup
        self.ck = ClickHouseAvailibility(self.driver)
        observedResult=self.ck.no_of_table()
        Assert.true(observedResult,'66')
        self.driver.close()