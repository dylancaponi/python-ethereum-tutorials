# Build a Dapp without metamask
# Transacting w blockchain costs ether / gas 
# Just reading from the blockchain is free
# User usually pays this transaction cost in metamask
# You could also have users initially fund their account
# Then make transactions on their behalf

from pprint import pprint

from web3 import Web3

from creds import infura_url

web3 = Web3(Web3.HTTPProvider(infura_url))

# What is preventing me from making infinite accounts?
account = web3.eth.account.create()

print(account.address)
print(account.privateKey)

# Create encrypted version of account
# Encryption password
PASSWORD = 'fakepassword'
keystore = account.encrypt(PASSWORD)

# Retrieve private key to sign transactions
web3.eth.account.decrypt(keystore, PASSWORD)

# Sign transaction
account.signTransaction()

# Get creative if you think there's a viable use case for this
# Seems like we really do need metamask in most cases
# We could only do transactions on a users behalf if we also
# somehow generated income from them using this app.