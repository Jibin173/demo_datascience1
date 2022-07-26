import pytest
from selenium import webdriver
from Utilities.customLogger import LogGen

@pytest.fixture()
def setup(browser):
    print("Launching chrome browser.........")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\josej\\Downloads\\chromedriver_win32(1)\chromedriver.exe")
        print("Launching chrome browser.........")
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'DataScience Project'
    config._metadata['Module Name'] = 'Test Framework'
    config._metadata['Tester'] = 'JIBIN JOSE'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
