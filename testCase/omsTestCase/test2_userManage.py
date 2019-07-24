# -*-coding:UTF-8-*-
# __author__ = 'gao'
from page.omsPage.login import *
from page.omsPage.userManage import *
from page.omsPage.init import *
import time


class TestUserManage(Init, Login, PinzhiUser):
    """用例：添加用户-保存"""
    def testcase1_addUser(self):
        self.username = self.getXMLData('omsUsername')
        self.pwd = self.getXMLData('omsPwd')
        self.login(self.username, self.pwd)
        time.sleep(2)

        # 添加新用户
        self.addUser('123456', 'autoTest')
        time.sleep(2)
        # 查询添加的用户
        self.searchUser("autoTest", "全部")
        time.sleep(2)
        self.assertTrue(self.isSearchResult(), '用户是否添加成功断言')

    """用例：查询用户"""
    def testcase2_searchUser(self):
        # 查询用户
        self.searchUser("autoTest", "全部")
        time.sleep(2)
        self.assertTrue(self.isSearchResult(), '查询用户断言')

    """用例：删除用户"""
    def testcase3_delUser(self):
        # 查询用户
        self.searchUser("autoTest", "全部")
        if(self.isSearchResult()):
            pass




if __name__ == '__main__':
    unittest.main(verbosity=2)
