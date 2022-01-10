from brownie import FundMe,MockV3Aggregator, network, config
from scripts import helpful_scripts


def deploy_fund_me():
    account = helpful_scripts.get_account()
    
    if network.show_active() not in helpful_scripts.LOCAL_BLOCKCHAIN_NETWORKS:
            price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        helpful_scripts.deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    contract = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()]["verify"])

    print(f"Contract deployed to {contract.address}")
    return contract

def main(): 
    deploy_fund_me()