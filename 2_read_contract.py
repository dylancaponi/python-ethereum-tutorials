# From Dapp University https://www.youtube.com/watch?v=prInJEq6JeI

# Standard python libraries
import json

# 3rd party libraries
from web3 import Web3

# Custom libraries
from creds import infura_url

web3 = Web3(Web3.HTTPProvider(infura_url))

# ABI is a JSON array that describes what the smart contract looks like
# Can be found on the Contract tab on etherscan.io:
# https://etherscan.io/address/0xd26114cd6EE289AccF82350c8d8487fedB8A0C07#code
with open('omg_abi.json') as f:
	abi = json.load(f)

# Address of the deployed smart contract on the blockchain
ADDRESS = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"

# Retrieve the contract
contract = web3.eth.contract(address=ADDRESS, abi=abi)
print(contract)

total_supply = contract.functions.totalSupply().call()

# This isn't ether but it also has 18 decimal places
# So we're treating it the same
print(web3.fromWei(total_supply, 'ether'))

# Let's print some properties of the contract
contract.functions.name().call()
contract.functions.symbol().call()

# Holders addresses can be found here:
# https://etherscan.io/token/0xd26114cd6EE289AccF82350c8d8487fedB8A0C07#balances
big_omg_wallet = Web3.toChecksumAddress('0x2551d2357c8da54b7d330917e0e769d33f1f5b93')
balance = contract.functions.balanceOf(big_omg_wallet).call()
print(web3.fromWei(balance, 'ether'))
