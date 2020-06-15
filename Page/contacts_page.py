from Common.basepage import BasePage
from Config.contact_info_xpath import *


class AddContactPage(BasePage):
    """添加联系人Page"""
    def init_add(self):
        # 底部通讯录按钮
        contact_button = self.by_uiautomator('new UiSelector().text("通讯录")')
        contact_button.click()
        # 左上角添加按钮
        add_button = self.by_id("iv_contact_add")
        add_button.click()

    def input_info(self, name, email, company, department, position, phone, addr, note):
        if name:
            el_name = self.by_xpath(xpath1)
            el_name.send_keys(name)
        if email:
            el_email = self.by_xpath(xpath2)
            el_email.send_keys(email)
        if company:
            el_company = self.by_xpath(xpath3)
            el_company.send_keys(company)
        if department:
            el_dep = self.by_xpath(xpath4)
            el_dep.send_keys(department)
        if position:
            el_pos = self.by_xpath(xpath5)
            el_pos.send_keys(position)
        if phone:
            el_pho = self.by_xpath(xpath6)
            el_pho.send_keys(phone)
        if addr:
            el_addr = self.by_xpath(xpath7)
            el_addr.send_keys(addr)
        if note:
            el_note = self.by_xpath(xpath8)
            el_note.send_keys(note)

    def save_button(self):
        el_save = self.by_id("tv_done")
        el_save.click()

