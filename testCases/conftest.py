from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Downloads\\chromedriver.exe")
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\Admin\\Downloads\\geckodriver.exe")
    else:
        print("IE driver")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############ pytest html Repott ##############

def pytest_configure(config):
    config._metadata['Project Name'] = 'Selenium Python'
    config._metadata['Module Name'] = "Learning"
    config._metadata['Tester'] = 'Murali'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
