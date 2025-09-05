from pages.base_page import BasePage
from utils.data_generator import random_username

class RegisterPage(BasePage):

    def register_user(self, first="First name", last="Last name", password="Password"):
        """
        填写注册表单并提交，返回 username 和 password
        """
        username = random_username()  # 生成随机唯一用户名
        address = "the 5th ring street"
        city = "Taiyuan"
        state = "Shanxi"
        zip_code = "041000"
        ssn = "1101142013"

        # 填写表单
        self.page.fill("#customer\\.firstName", first)
        self.page.fill("#customer\\.lastName", last)
        self.page.fill("#customer\\.username", username)
        self.page.fill("#customer\\.password", password)
        self.page.fill("#repeatedPassword", password)
        self.page.fill("#customer\\.address\\.street", address)
        self.page.fill("#customer\\.address\\.city", city)
        self.page.fill("#customer\\.address\\.state", state)
        self.page.fill("#customer\\.address\\.zipCode", zip_code)
        self.page.fill("#customer\\.ssn", ssn)

        # 点击 Register
        self.page.click("input[value='Register']")

        # 返回生成的用户名和密码
        return username, password

    # def logout(self):
    #     # 点击 "Log Out"
    #     self.page.click("a[href*='logout.htm']")
    #     # 返回首页对象
    #     return HomePage(self.page)