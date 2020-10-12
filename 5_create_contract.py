# Instructions
# Install and open Ganache: https://www.trufflesuite.com/ganache
# Go to remix.ethereum.org
# Copy contents of 4_greeter.sol into a new file
# Check that compiler version matches pragma solidity version in code
# Compile and copy ABI to 4_abi.json and
# copy bytecode to 5_bytecode.json from bottom of panel


import json

from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Use default account. It's unlocked so no private key needed.
web3.eth.defaultAccount = web3.eth.accounts[0]


# A lot of complication in compiling on your computer
# due to current tooling
# Instead, use remix
with open('4_abi.json', 'r') as f:
    abi = json.load(f)

with open('5_bytecode.json', 'r') as f:
    bytecode = json.load(f)['object']

# Instantiate contract
Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy contract
tx_hash = Greeter.constructor().transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Instantiate contract
contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
    )

print(contract.functions.greet().call())

# Update greeting
tx_hash = contract.functions.setGreeting('Greeting #2').transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(contract.functions.greet().call())
