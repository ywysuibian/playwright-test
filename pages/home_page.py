from pages.base_page import BasePage
from pages.register_page import RegisterPage


class HomePage:
    def __init__(self, page):
        self.page = page

    def goto(self, base_url: str):
        self.page.goto(base_url)

    def get_title(self):
        return self.page.title()
    
    def go_to_register(self):
        self.page.click("a[href='register.htm']")
        return RegisterPage(self.page)