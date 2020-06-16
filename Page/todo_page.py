from Common.basepage import BasePage


class ToDoPage(BasePage):
    """新建待办Page"""
    def cancel_failure(self):
        text_source = self.by_class("android.widget.TextView")
        text_value = []
        for i in text_source:
            text_value.append(i.text)
        text_ass = "".join(text_value)
        if "未发送成功的邮件" in text_ass:
            self.by_id("alert_dialog_content_msg").click()

    def func_select(self):
        # 右上角加号
        func_button = self.by_id("iv_mail_list_plus")
        func_button.click()
        write_button = self.by_id("tv_new_todo")
        write_button.click()

    def new_todo(self, todo):
        todo_input = self.by_id("et_todo_content")
        todo_input.send_keys(todo)
        done_button = self.by_id("btn_done")
        done_button.click()
