import unittest
import os
from time import sleep
from appium import webdriver
from ddt import ddt, data, unpack
from Config.app_config import Desired_Capabilities
from TestAction.add_todo import AddToDo
from Utils.exceldealutil import ParseExcel

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = base_dir + '\\TestData\\add_todo.xlsx'
sheetname = 'Sheet1'
excel = ParseExcel(excelpath, sheetname)


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
        action = AddToDo(self.driver)
        action.add_new_todo(todo)
        # 是否获取到正确的toast
        toast = action.is_toast_exist(self.driver, assertion)
        self.assertEqual(True, toast)
        sleep(2)


if __name__ == '__main__':
    unittest.main()
