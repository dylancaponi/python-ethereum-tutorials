# Instructions
# Install and open Ganache
# Use remix.ethereum.org and copy / paste contents of 4_greeter.sol
# Set compile version to match pragma solidity version below
# Set environment to web3 provider and port to match RPC server in Ganache
# Hit deploy and you will see a contract in Ganache transactions
# Copy deployed contract_address from remix.ethereum.org under deployed contracts
# Copy ABI from bottom of compile tab in remix.ethereum.org
# Create empty 4_abi.json
# Paste ABI into 4_abi.json

import json

from web3 import Web3

# Connect to Ganache and use first account
# No private key required because this account is unlocked
GANACHE_URL = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))
web3.eth.defaultAccount = web3.eth.accounts[0]

contract_address = web3.toChecksumAddress('<see instructions above>')

with open('4_abi.json', 'r') as f:
    contract_abi = json.load(f)

# Instantiate contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Read greeting
print(f"Original greeting: {contract.functions.greet().call()}")

# Set new greeting
# This cost ~.00025eth or ~$0.09 (1eth=$350) on Ganache.
# This price seems high to me, can anyone weigh in?
tx_hash = contract.functions.setGreeting('I paid $0.09 to change this').transact()

print(f"Transaction hash: {tx_hash}")

# Wait for transaction receipt
web3.eth.waitForTransactionReceipt(tx_hash)

# Read greeting again
print(f"Updated greeting: {contract.functions.greet().call()}")