from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_NETWORKS
from brownie import network, accounts, exceptions
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    contract = deploy_fund_me()
    entrance_fee = contract.getEntranceFee() + 100
    tx1 = contract.fund({"from": account, "value": entrance_fee})
    tx1.wait(1)
    assert contract.addressToAmountFunded(account) == entrance_fee, f"Address: {account}, Entrance Fee: {entrance_fee}"
    tx2 = contract.withdraw({"from": account})
    tx2.wait(1)
    assert contract.addressToAmountFunded(account) == 0, f"Address: {account}"


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})

