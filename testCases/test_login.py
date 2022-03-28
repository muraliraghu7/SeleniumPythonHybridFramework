import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.customLogger import LogGen


class Test_login:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    log = LogGen.getLogger()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.log.info("Opened the app url")
        act_title = self.driver.title
        self.log.info('The page title is: ' + act_title)

        if act_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.log.info("Opened the app url")
        lp = LoginPage(self.driver)
        lp.setUserName(self.email)
        self.log.info("Entered the User name")
        lp.setPassword(self.password)
        self.log.info("Entered the Password")
        lp.clickLogin()
        act_title = self.driver.title
        lp.clickLogout()
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
