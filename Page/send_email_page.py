from Common.basepage import BasePage


class SendEmailPage(BasePage):
    """发送邮件Page"""
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
        write_button = self.by_id("tv_write_mail")
        write_button.click()

    def write_email(self, email, topic, text):
        email_input = self.by_id("mailcompose_address_input")
        email_input.send_keys(email)
        if topic:
            topic_input = self.by_id("mailcompose_subject_textedit")
            topic_input.send_keys(topic)
        if text:
            text_input = self.by_class("android.widget.EditText")
            text_input[2].send_keys(text)

    def send_click(self):
        send_button = self.by_id("send")
        send_button.click()
