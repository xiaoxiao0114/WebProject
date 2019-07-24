# -*- coding:UTF-8 -*-
from base.basePage import *
from selenium.webdriver.common.by import By


class PageLogin(WebDriver):
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    login_loc = (By.ID, 'btnLogin')
    loginError_loc = (By.XPATH, '//*[@id="loginForm"]/div[1]/div')

    def typeUsername(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self, password):
        self.findElement(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self, username, password):
        self.typeUsername(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getLoginError(self):
        return self.findElement(*self.loginError_loc).text

