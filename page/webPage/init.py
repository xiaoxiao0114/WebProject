# -*- coding:UTF-8 -*-
from selenium import webdriver
from utils.readXML import *
import unittest
"""测试固件分离"""

class Init(unittest.TestCase, ReadXML):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(self.getXMLData('weburl'))

    def tearDown(self):
        self.driver.quit()