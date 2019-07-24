# -*- coding:UTF-8 -*-
"""web端管理系统登录"""
from page.webPage.p_login import *
from page.webPage.init import *
import time
from assertpy import assert_that


class WebPcLogin(Init, PageLogin):
    def test_webPcLogin01(self):
        """登录，输入错误的用户名和密码"""
        self.login('d', 'd')
        time.sleep(3)
        # print(self.getLoginError)
        assert_that(self.getLoginError).is_equal_to("用户名或密码错误")
        # self.assertEqual(self.getLoginError, "用户名或密码错误")


if __name__ == '__main__':
    unittest.main(verbosity=2)