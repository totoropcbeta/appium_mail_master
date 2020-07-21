import logging
import traceback
import unittest
import os
from time import sleep
from appium import webdriver
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException

from Config.app_config import Desired_Capabilities
from TestAction.send_email import SendEmail
from Utils.exceldealutil import ParseExcel


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = base_dir + '/TestData/write_email_info.xlsx'
sheetname = 'Sheet1'
excel = ParseExcel(excelpath, sheetname)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='mail_master_test.log',
                    filemode='a+',
                    )


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
        try:
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
        except NoSuchElementException as e:
            logging.error("页面元素不存在,异常堆栈信息:" + str(traceback.format_exc()))

        except AssertionError as e:
            logging.info("测试用例:%s, 期望: \'%s\',, 失败" % ((email, topic, text), assertion))

        except Exception as e:
            logging.error("未知错误, 错误信息:" + str(traceback.format_exc()))
        else:
            logging.info("测试用例:%s, 期望: \'%s\', 通过" % ((email, topic, text), assertion))


if __name__ == '__main__':
    unittest.main()
