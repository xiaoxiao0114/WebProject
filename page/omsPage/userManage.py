# -*-coding:UTF-8-*-
# __author__ = 'gao'
from base.basePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class PinzhiUser(WebDriver):
    """品智用户管理界面"""
    """用户名（查询）"""
    username_loc = (By.ID, 'username')
    """权限（查询）"""
    authority_loc = (By.ID, 'privilege')
    """查询按钮"""
    search_loc = (By.ID, 'btnSearch')
    """查询的结果"""
    searchResult_loc = (By.CSS_SELECTOR, '#user > tbody > tr > td')
    """添加品智用户+"""
    addUser_loc = (By.ID, 'addBtn')
    """重置密码"""
    reset_loc = (By.NAME, 'btnReset')
    """修改"""
    change_loc = (By.NAME, 'btnChg')
    """停用"""
    disable_loc = (By.NAME, 'btnDisable')
    """删除"""
    delete_loc = (By.NAME, 'btnDelete')


    """添加+按钮"""
    def clickAddUser(self):
        self.findElement(*self.addUser_loc).click()

    """输入要查询的用户名"""
    def typeUsername(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    """选择要查询的权限，下拉框"""
    def selectAuthority(self, authority):
        self.select_element = self.findElement(*self.authority_loc)
        self.select = Select(self.select_element)
        self.select.select_by_visible_text(authority)

    """查询功能"""
    def searchUser(self, username, authority):
        self.typeUsername(username)
        self.selectAuthority(authority)
        self.findElement(*self.search_loc).click()

    def isSearchResult(self):
        self.rel = self.findElement(*self.searchResult_loc).text
        if self.rel == "表中数据为空":
            return False
        else:
            return True

    """添加品智用户界面"""
    """输入工号属性"""
    employeeNo_loc = (By.ID, 'epno')
    """输入用户名属性"""
    employeeName_loc = (By.ID, 'epname')
    """选择权限"""
    selectAuth_loc = (By.XPATH, '//*[@id="_easyui_tree_1"]/span[3]')  #全部权限
    """保存按钮属性"""
    save_loc = (By.ID, 'btnSave')

    """输入工号"""
    def typeEmployeeNo(self, employeeNo):
        self.findElement(*self.employeeNo_loc).send_keys(employeeNo)

    """输入用户名"""
    def typeEmployeeName(self, employeeName):
        self.findElement(*self.employeeName_loc).send_keys(employeeName)

    """选择权限"""
    def selectAuth(self):
        self.findElement(*self.selectAuth_loc).click()

    """保存"""
    @property
    def save(self):
        self.findElement(*self.save_loc).click()

    """添加用户"""
    def addUser(self, employeeNo='123456', employeeName='autoTest'):
        self.clickAddUser()
        time.sleep(2)
        self.typeEmployeeNo(employeeNo)
        self.typeEmployeeName(employeeName)
        self.selectAuth()
        self.save








