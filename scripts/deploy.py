from brownie import Lottery, accounts
from scripts.helper_script import get_accounts, get_contracts


def main():
    pass


def deploy_lottery():
    lottery = Lottery.deploy({"from": accounts[0]})
