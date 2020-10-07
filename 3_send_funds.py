# From Dapp University: https://www.youtube.com/watch?v=jA0sL3PM2DE

from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())
print(web3.eth.blockNumber())

# We're using this test net so no real funds are used
# https://truffleframework.com/ganache

# Send funds from here
ACCOUNT_1 = ''
# Authorization to send funds
private_key = ''

# Receive funds here
ACCOUNT_2 = ''

# Get the nonce
# Prevents you from sending transaction twice
nonce = web3.eth.getTransactionCount(ACCOUNT_1)

# Build a transaction
tx = {
	'nonce': nonce,
	'to': ACCOUNT_2,
	'value': web3.toWei(1, 'ether'),
	'gas': 2000000,
	'gasPrice': web3.toWei('50', 'gwei')
}

# Sign a transaction
# Don't have to pass ACCOUNT_1 because
# it can be built from the private_key
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# Send a transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Get a transaction hash
print(web3.toHex(tx_hash))
