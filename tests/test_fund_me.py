from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account
def test_can_fund_and_withdraw():
    account = get_account()
    contract = deploy_fund_me()
    entrance_fee = contract.getEntranceFee()
    tx1 = contract.fund({"from": account, "value": entrance_fee})
    tx1.wait(1)
    assert contract.addressToAmountFunded(account) == entrance_fee, f"Address: {account}, Entrance Fee: {entrance_fee}"
    tx2 = contract.withdraw({"from": account})
    tx2.wait(1)
    assert contract.addressToAmountFunded(account) == 0, f"Address: {account}"
