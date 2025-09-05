from pages.base_page import BasePage

class AccountPage(BasePage):
    def open_new_account(self, account_type="SAVINGS"):
        self.page.select_option("#type", account_type)
        self.page.click("input[value='Open New Account']")
        new_account = self.page.inner_text("#newAccountId")
        return new_account

    def is_account_balance_displayed(self, account_id):
        # 示例：检查账户概览页面是否显示余额
        return self.page.is_visible(f"text={account_id}")
