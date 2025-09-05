from pages.base_page import BasePage

class TransferPage(BasePage):
    def transfer_funds(self, from_acc, to_acc, amount):
        self.page.fill("#fromAccountId", from_acc)
        self.page.fill("#toAccountId", to_acc)
        self.page.fill("#amount", str(amount))
        self.page.click("input[value='Transfer']")
