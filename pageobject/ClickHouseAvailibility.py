import pytest
from clickhouse_driver import Client


class ClickHouseAvailibility:

    def __init__(self, driver):
        self.driver = driver

    def databaseactivity(self):
        try:
            print("enter")
            client = Client(host='164.52.218.88', user='default', password='carinov', port=9000, database='hittachi')
            RESULT = client.execute("SHOW TABLES")
            return RESULT
        except:
            pytest.fail("Unable to connect the clickhouse database")


    def no_of_table(self):
        try:
                print("enter")
                client = Client(host='164.52.218.88', user='default', password='carinov', port=9000,
                                database='hittachi')
                RESULT = client.execute("SHOW TABLES")
                print(RESULT)
                print(len(RESULT))
                return len(RESULT)
        except:
                pytest.fail("Unable to connect the clickhouse database")
