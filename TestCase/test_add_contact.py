import unittest
import os
from time import sleep
from appium import webdriver
from ddt import ddt, data, unpack
from Config.app_config import Desired_Capabilities
from TestAction.add_contact import AddContact
from Utils.exceldealutil import ParseExcel
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = base_dir + '/TestData/contact_info.xlsx'
sheetname = 'Sheet1'
excel = ParseExcel(excelpath, sheetname)


@ddt
class TestAddContact(unittest.TestCase):
    """添加联系人测试"""
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
    def test_new_contact(self, name, email, company, department, position, phone, addr, note, assertion):
        action = AddContact(self.driver)
        action.add_contact(name, email, company, department, position, phone, addr, note)
        sleep(2)
        text_source = self.driver.find_elements_by_class_name("android.widget.TextView")
        text_value = []
        for i in text_source:
            text_value.append(i.text)
        self.assertIn(assertion, text_value)
        if assertion == '请填写正确的邮箱地址':
            self.driver.keyevent(4)
            self.driver.keyevent(4)
        else:
            self.driver.keyevent(4)


if __name__ == '__main__':
    unittest.main()
