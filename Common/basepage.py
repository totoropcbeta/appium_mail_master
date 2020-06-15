class BasePage:
    """封装appium常见的元素定位方法"""
    def __init__(self, driver):
        self.driver = driver

    # id 定位
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    # class 定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    # xpath 定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # accessibility id 定位
    def by_acid(self, acid):
        return self.driver.find_element_by_accessibility_id(acid)

    # android uiautomator 定位
    def by_uiautomator(self, ui):
        return self.driver.find_element_by_android_uiautomator(ui)

    # 模拟返回键
    def back(self):
        return self.driver.keyevent(4)

    # 获取所有元素class属性为class_name的文本内容
    def cur_text(self, class_name):
        return self.driver.find_element_by_class_name(class_name)
