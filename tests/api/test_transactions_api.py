import pytest
import requests
from utils.config import BASE_URL

def test_find_transactions_by_amount():
    # 从 UI 测试保存的账号信息读取
    with open("account_info.txt") as f:
        username, password, account_id = f.read().strip().split(",")

    url = f"{BASE_URL}/parabank/services/bank/findTransactions"
    params = {"accountId": account_id, "amount": "50"}
    resp = requests.get(url, params=params)
    assert resp.status_code == 200
    data = resp.json()
    assert "transaction" in data
