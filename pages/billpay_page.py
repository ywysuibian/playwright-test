from pages.base_page import BasePage

class BillPayPage(BasePage):
    def pay_bill(self, from_acc, payee_name, amount):
        self.page.fill("#fromAccountId", from_acc)
        self.page.fill("#payee.name", payee_name)
        self.page.fill("#amount", str(amount))
        self.page.click("input[value='Send Payment']")
