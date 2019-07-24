# -*-coding:UTF-8-*-
# __author__ = 'gao'
from base.basePage import *
from selenium.webdriver.common.by import By


class Title(WebDriver):
    """餐行健.品智管理系统登录后组织架构、用户管理等标题类"""
    operationManager_loc = (By.XPATH, "//*[@id='DH']/li[3]/a")

    '''点击营运管理'''
    def clickOperationManager(self):
        self.findElement(*self.operationManager_loc).click()

