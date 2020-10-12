# web3 library can recreate everything on etherscan

from pprint import pprint

from web3 import Web3

from creds import infura_url



web3 = Web3(Web3.HTTPProvider(infura_url))

# Get block number
latest_block = web3.eth.blockNumber
print(latest_block)

# Get block info - equivalent to Latest Blocks on etherscan
print(web3.eth.getBlock(latest_block))

# Get info on last 10 blocks
for i in range(0, 10):
  print(web3.eth.getBlock(latest - i))

# See transactions on a block
# To get block hash from etherscan
# Click on a block number
# Click to see more -> Hash:
hash = ''
print(web3.eth.getTransactionByBlock(hash, 5))