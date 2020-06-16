from Page.send_email_page import SendEmailPage


class SendEmail(SendEmailPage):
    """发送邮件"""
    def send_email(self, email, topic, text):
        se = SendEmailPage(self.driver)
        se.cancel_failure()
        se.func_select()
        se.write_email(email, topic, text)
        se.send_click()
