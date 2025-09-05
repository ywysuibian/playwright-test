import pytest
from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.transfer_page import TransferPage
from pages.billpay_page import BillPayPage
from utils.config import BASE_URL

def test_parabank_e2e_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)  # 用本地 Chrome
        page = browser.new_page()

        # step 1, open Para bank home page
        home_page = HomePage(page)
        home_page.goto(BASE_URL)
        assert "ParaBank" in home_page.get_title()

        # step 2, create a new user
        register_page = home_page.go_to_register()
        assert page.locator("h1.title").text_content() == "Signing up is easy!"

        username, password = register_page.register_user()
        assert page.locator("h1.title").text_content() == "Welcome " + username
        register_page.page.wait_for_timeout(1000)

        # home_page = register_page.logout()

        # step 3, login


        '''  
      
        # 3. 登录
        login_page = LoginPage(page)
        login_page.goto(BASE_URL + "parabank/login.htm")
        login_page.login(username, password)
        
        # 4. 验证主页全局导航
        assert home_page.is_navigation_menu_visible()
        
        # 5. 开户
        account_page = AccountPage(page)
        account_page.goto(BASE_URL + "parabank/openaccount.htm")
        new_account = account_page.open_new_account()
        
        # 6. 验证账户概览显示余额
        assert account_page.is_account_balance_displayed(new_account)
        
        # 7. 转账
        transfer_page = TransferPage(page)
        transfer_page.goto(BASE_URL + "parabank/transfer.htm")
        transfer_page.transfer_funds(from_acc=new_account, to_acc="12345", amount=100)
        
        # 8. 支付账单
        billpay_page = BillPayPage(page)
        billpay_page.goto(BASE_URL + "parabank/billpay.htm")
        billpay_page.pay_bill(from_acc=new_account, payee_name="Test Payee", amount=50)
        
        # 保存信息供 API 测试
        with open("account_info.txt", "w") as f:
            f.write(f"{username},{password},{new_account}")
        '''
