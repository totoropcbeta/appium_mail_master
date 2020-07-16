import unittest
import os
from time import sleep
from appium import webdriver
from ddt import ddt, data, unpack
from Config.app_config import Desired_Capabilities
from TestAction.send_email import SendEmail
from Utils.exceldealutil import ParseExcel
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = base_dir + '/TestData/write_email_info.xlsx'
sheetname = 'Sheet1'
excel = ParseExcel(excelpath, sheetname)


@ddt
class TestSendEmail(unittest.TestCase):
    """写邮件测试"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Desired_Capabilities)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    @data(*excel.getdatasfromsheet())
    @unpack
    def test_send_email(self, email, topic, text, assertion):
        action = SendEmail(self.driver)
        action.send_email(email, topic, text)
        sleep(5)
        text_source = self.driver.find_elements_by_class_name("android.widget.TextView")
        text_value = []
        for i in text_source:
            text_value.append(i.text)
        text_ass = "".join(text_value)
        self.assertIn(assertion, text_ass)
        if assertion == "不是有效的邮箱地址":
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            sleep(1)
            self.driver.find_element_by_id("alert_dialog_btnCancel").click()
        elif assertion == "收件人不存在":
            self.driver.keyevent(4)


if __name__ == '__main__':
    unittest.main()
