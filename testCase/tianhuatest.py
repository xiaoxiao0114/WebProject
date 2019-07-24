import time
from page.webPage.init import *
from page.webPage.p_login import *
from page.operationManager.sysMaintenance import *
from page.webPage.p_title import *


class Pinzhitest1(Init, PageLogin, SysMaintenance, Title):
    def testPlan(self):
        # 登录
        self.login(self.getXMLData('username'), self.getXMLData('password'))
        time.sleep(3)

        # assertpy.assert_that(self.driver.page_source).contains('logout')

        # 进入页面
        self.clickOperationManager()
        time.sleep(1)
        self.clickSysMaintenance()
        time.sleep(1)
        self.makeSalePlan()
        time.sleep(1)
        self.selectShop()
        time.sleep(2)
        self.currentFiscalYear()
        time.sleep(1)
        self.actualBusinessIncome()
        time.sleep(5)
        actualVal = self.findElement(*self.viewSalePlan_loc).text
        expect = "开始制定销售计划"
        try:
            self.assertEqual(expect, actualVal, "开始制定销售计划文字断言失败！")
        except AssertionError:
            self.viewSalePlan()
        # finally:
        #     self.viewSalePlan()
        print("************")
        time.sleep(10)
        # assertpy.assert_that()
        # btn_text1 = self.driver.find_element_by_id("planbtn").text
        # self.assertEqual(btn_text1,"开始制定销售计划","按钮文字错误！")  # 断言按钮文字
        # self.driver.find_element_by_id("planbtn").click()   # 进入门店计划页面
        # time.sleep(2)
        # assert "【营业实收】销售计划制定" in self.driver.page_source, "进入制定实收计划页面失败！"
        # self.driver.find_element_by_id("finacevalue").send_keys("80000000")
        # self.driver.find_element_by_id("1_1_v").send_keys("1000")
        # self.driver.find_element_by_id("2_2_v").send_keys("2000")
        # self.driver.find_element_by_id("3_3_v").send_keys("3000")
        # self.driver.find_element_by_id("save").click()     # 保存
        # time.sleep(2)
        #
        # # 修改
        # self.driver.find_element_by_xpath("//*[@id='ognidListDiv']/li[16]/a").click()   # 再次选择门店
        # time.sleep(2)
        # self.driver.find_element_by_id("fyear").click() # 当前财年
        # self.driver.find_element_by_id("ftype").click() # 营业实收
        # btn_text2 = self.driver.find_element_by_id("planbtn").text
        # self.assertEqual(btn_text2,"查看销售计划","保存计划失败or按钮文字显示错误")  # 断言按钮文字
        #
        # self.driver.find_element_by_id("planbtn").click()   # 进入门店计划页面
        # time.sleep(2)
        # assert "【营业实收】销售计划制定" in self.driver.page_source, "进入制定实收计划页面失败！"
        # finacevalue1 = self.driver.find_element_by_id("finacevalue").get_attribute("value")
        # self.assertEqual(finacevalue1,"80000000","保存计划额失败or文本框未回显计划额")
        # value1_1_1 = self.driver.find_element_by_id("1_1_v").get_attribute("value")
        # value1_2_2 = self.driver.find_element_by_id("2_2_v").get_attribute("value")
        # value1_3_3 = self.driver.find_element_by_id("3_3_v").get_attribute("value")
        # self.assertEqual(value1_1_1,"1000","1月1日保存失败or文本框未回显")
        # self.assertEqual(value1_2_2,"2000","2月2日保存失败or文本框未回显")
        # self.assertEqual(value1_3_3,"3000","3月3日保存失败or文本框未回显")
        #
        # # 清空
        # self.driver.find_element_by_id("finacevalue").clear()
        # self.driver.find_element_by_id("1_1_v").clear()
        # self.driver.find_element_by_id("2_2_v").clear()
        # self.driver.find_element_by_id("3_3_v").clear()    # 清空文本框保存信息
        # # 重新设置
        # self.driver.find_element_by_id("finacevalue").send_keys("88888888")
        # self.driver.find_element_by_id("1_1_v").send_keys("11000")
        # self.driver.find_element_by_id("2_2_v").send_keys("22000")
        # self.driver.find_element_by_id("3_3_v").send_keys("33000")
        # self.driver.find_element_by_id("31_12_v").send_keys("12000")
        # self.driver.find_element_by_id("save").click()     # 保存
        # time.sleep(2)
        #
        # # 断言是否保存成功
        # self.driver.find_element_by_xpath("//*[@id='ognidListDiv']/li[16]/a").click()   # 再次选择门店
        # time.sleep(2)
        # self.driver.find_element_by_id("fyear").click() # 当前财年
        # self.driver.find_element_by_id("ftype").click() # 营业实收
        # btn_text3 = self.driver.find_element_by_id("planbtn").text
        # self.assertEqual(btn_text3,"查看销售计划","保存计划失败or按钮文字显示错误")  # 断言按钮文字
        #
        # self.driver.find_element_by_id("planbtn").click()   # 进入门店计划页面
        # time.sleep(2)
        # assert "【营业实收】销售计划制定" in self.driver.page_source, "进入制定实收计划页面失败！"
        # finacevalue1 = self.driver.find_element_by_id("finacevalue").get_attribute("value")
        # self.assertEqual(finacevalue1,"88888888","保存计划额失败or文本框未回显计划额")
        # value2_1_1 = self.driver.find_element_by_id("1_1_v").get_attribute("value")
        # value2_2_2 = self.driver.find_element_by_id("2_2_v").get_attribute("value")
        # value2_3_3 = self.driver.find_element_by_id("3_3_v").get_attribute("value")
        # value2_31_12 = self.driver.find_element_by_id("31_12_v").get_attribute("value")
        # self.assertEqual(value2_1_1,"11000","1月1日保存失败or文本框未回显")
        # self.assertEqual(value2_2_2,"22000","2月2日保存失败or文本框未回显")
        # self.assertEqual(value2_3_3,"33000","3月3日保存失败or文本框未回显")
        # self.assertEqual(value2_31_12,"12000","12月31日保存失败or文本框未回显")
        # time.sleep(2)
        #
        # # 下发到门店
        # self.driver.find_element_by_id("send").click()
        # time.sleep(1)
        # confirmvalue = self.driver.find_element_by_id("confirmvalue").text
        # self.assertEqual(confirmvalue,"88,888,888元","弹窗内容错误")
        # canceltext = self.driver.find_element_by_id("cancel").text
        # self.assertEqual(canceltext,"再考虑会","按钮文字错误！")
        # self.driver.find_element_by_id("cancel").click()    # 再考虑会
        # time.sleep(1)
        #
        # self.driver.find_element_by_id("send").click()
        # time.sleep(1)
        # confirmvalue = self.driver.find_element_by_id("confirmvalue").text
        # self.assertEqual(confirmvalue,"88,888,888元","弹窗内容错误")
        # canceltext = self.driver.find_element_by_id("enter").text
        # self.assertEqual(canceltext,"确认下发","按钮文字错误！")
        # self.driver.find_element_by_id("enter").click()     # 确认下发
        # time.sleep(1)
        #
        # # 断言是否下发成功
        # self.driver.find_element_by_xpath("//*[@id='ognidListDiv']/li[16]/a").click()  # 再次选择门店
        # time.sleep(2)
        # self.driver.find_element_by_id("fyear").click()  # 当前财年
        # self.driver.find_element_by_id("ftype").click()  # 营业实收
        # btn_text4 = self.driver.find_element_by_id("planbtn").text
        # self.assertEqual(btn_text4, "查看销售计划", "保存计划失败or按钮文字显示错误")  # 断言按钮文字
        #
        # self.driver.find_element_by_id("planbtn").click()  # 进入门店计划页面
        # time.sleep(2)
        # assert "【营业实收】销售计划制定" in self.driver.page_source, "进入制定实收计划页面失败！"
        # sendvalue = self.driver.find_element_by_id("sendvalue").text
        # self.assertEqual(sendvalue, "88,888,888", "回显值错误")      # 计划额回显示
        # value3_1_1 = self.driver.find_element_by_id("1_1_v").get_attribute("value")
        # value3_2_2 = self.driver.find_element_by_id("2_2_v").get_attribute("value")
        # value3_3_3 = self.driver.find_element_by_id("3_3_v").get_attribute("value")
        # value3_31_12 = self.driver.find_element_by_id("31_12_v").get_attribute("value")
        # self.assertEqual(value3_1_1,"11000","1月1日保存失败or文本框未回显")
        # self.assertEqual(value3_2_2,"22000","2月2日保存失败or文本框未回显")
        # self.assertEqual(value3_3_3,"33000","3月3日保存失败or文本框未回显")
        # self.assertEqual(value3_31_12,"12000","12月31日保存失败or文本框未回显")     # 参考值回显
        # explain = self.driver.find_element_by_id("explain").text
        # self.assertEqual(explain,"计划已下发至门店，不可修改","下发后显示内容有误")   # 下发后的文字内容
        # self.driver.find_element_by_id("1_2_v").get_attribute("readonly")   # 文本框只读
        # time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
