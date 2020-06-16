from Page.todo_page import ToDoPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AddToDo(ToDoPage):
    """新建代办"""
    def add_new_todo(self, todo):
        td = ToDoPage(self.driver)
        td.cancel_failure()
        td.func_select()
        td.new_todo(todo)

    def is_toast_exist(self, driver, text=None, timeout=30, poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(ec.presence_of_element_located(toast_loc))
            return True
        except:
            return False
