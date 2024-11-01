import eth_account
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()
    
    # Generate a new Ethereum account
    account = Account.create()
    eth_address = account.address  # Account address derived from public key
    private_key = account.privateKey  # Account private key for signing
    
    # Encode the message
    message = encode_defunct(text=m)
    
    # Sign the message using the private key
    signed_message = Account.sign_message(message, private_key=private_key)
    
    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)
    
    return eth_address, signed_message
