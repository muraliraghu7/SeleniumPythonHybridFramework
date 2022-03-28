from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    email = (By.NAME, "Email")
    password = (By.ID, "Password")
    login = (By.XPATH, "//button[text()='Log in']")
    logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userName):
        self.driver.find_element(*LoginPage.email).clear()
        self.driver.find_element(*LoginPage.email).send_keys(userName)

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.password).clear()
        self.driver.find_element(*LoginPage.password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LoginPage.login).click()

    def clickLogout(self):
        self.driver.find_element(*LoginPage.logout).click()
