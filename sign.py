from eth_account import Account
from eth_account.messages import encode_defunct

def sign(m):
    account = Account.create()
    eth_address = account.address
    
    message = encode_defunct(text=m)
    
    signed_message = account.sign_message(message)
    
    return eth_address, signed_message
