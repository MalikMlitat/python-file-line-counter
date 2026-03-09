from playwright.sync_api import expect

class PIMPage:
    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.add_emp_link = page.get_by_role("link", name="Add Employee")
        
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.save_btn = page.get_by_role("button", name="Save")

    def add_employee(self, first, last):
        # 1. الدخول لقائمة PIM
        self.pim_menu.click()
        
        # 2. الضغط على إضافة موظف (استخدمنا نفس الاسم add_emp_link)
        self.add_emp_link.click()

        # 3. تعبئة البيانات
        self.first_name.fill(first)
        self.last_name.fill(last)

        # 4. الحفظ
        self.save_btn.click()

        # 5. التأكيد (Assertion) مع انتظار كافٍ
        expect(self.page.get_by_role("heading", name="Personal Details")).to_be_visible(timeout=10000)