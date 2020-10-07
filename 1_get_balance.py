# From Dapp University: https://www.youtube.com/watch?v=SAi5rYFh7yw

from web3 import Web3

from creds import infura_url

# This is a huge Kraken cold wallet
ETH_ADDRESS = "0x53d284357ec70cE289D6D64134DfAc8E511c8a3D"

# Create client connection
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
print(web3.isConnected())

# Current block number
print(web3.eth.blockNumber)

# Get balance
balance = web3.eth.getBalance(ETH_ADDRESS)

# Convert Wei to Ether
print(web3.fromWei(balance, "ether"))
