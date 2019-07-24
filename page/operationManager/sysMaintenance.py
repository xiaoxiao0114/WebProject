# -*-coding:UTF-8-*-
# __author__ = 'gao'
from base.basePage import *
from selenium.webdriver.common.by import By

class SysMaintenance(WebDriver):
    """点击营运管理，左侧菜单列"""
    sysMaintenance_loc = (By.XPATH, "//*[@id='headingDateImport']/h4/a")
    makeSalePlan_loc = (By.XPATH, "//*[@id='1829']")
    selectShop_loc = (By.XPATH, "//*[@id='ognidListDiv']/li[16]/a")  #列表第16个，目前是"品智微信点餐后付测试"
    currentFiscalYear_loc = (By.ID, "fyear")
    actualBusinessIncome_loc = (By.ID, "ftype")
    viewSalePlan_loc = (By.ID, "planbtn")

    '''点击系统维护'''
    def clickSysMaintenance(self):
        self.findElement(*self.sysMaintenance_loc).click()

    '''点击制定销售计划'''
    def makeSalePlan(self):
        self.findElement(*self.makeSalePlan_loc).click()

    '''选择门店'''
    def selectShop(self):
        self.findElement(*self.selectShop_loc).click()

    '''2019财年'''
    def currentFiscalYear(self):
        self.findElement(*self.currentFiscalYear_loc).click()

    '''营业实收'''
    def actualBusinessIncome(self):
        self.findElement(*self.actualBusinessIncome_loc).click()

    '''开始制定销售计划/查看销售计划'''
    def viewSalePlan(self):
        self.findElement(*self.viewSalePlan_loc).click()



