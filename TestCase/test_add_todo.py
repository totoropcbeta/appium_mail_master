import logging
import traceback
import unittest
import os
from time import sleep
from appium import webdriver
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException

from Config.app_config import Desired_Capabilities
from TestAction.add_todo import AddToDo
from Utils.exceldealutil import ParseExcel

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = base_dir + '/TestData/add_todo.xlsx'
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
    """新建待办测试"""
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
    def test_send_email(self, todo, assertion):
        try:
            action = AddToDo(self.driver)
            action.add_new_todo(todo)
            # 是否获取到正确的toast
            toast_flag = action.is_toast_exist(self.driver, assertion)
            self.assertEqual(True, toast_flag)
            sleep(2)
        except NoSuchElementException as e:
            logging.error("页面元素不存在,异常堆栈信息:" + str(traceback.format_exc()))

        except AssertionError as e:
            logging.info("测试用例:%s, 期望: \'%s\',, 失败" % (todo, assertion))

        except Exception as e:
            logging.error("未知错误, 错误信息:" + str(traceback.format_exc()))
        else:
            logging.info("测试用例:%s, 期望: \'%s\', 通过" % (todo, assertion))


if __name__ == '__main__':
    unittest.main()
