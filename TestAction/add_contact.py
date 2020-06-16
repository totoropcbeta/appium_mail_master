from Page.contacts_page import AddContactPage


class AddContact(AddContactPage):
    """添加联系人"""
    def add_contact(self, name, email, company, department, position, phone, addr, note):
        cp = AddContactPage(self.driver)
        cp.cancel_failure()
        cp.init_add()
        cp.input_info(name, email, company, department, position, phone, addr, note)
        cp.save_button()
