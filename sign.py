from eth_account import Account
from eth_account.messages import encode_defunct

def sign(m):
    # Generate a new Ethereum account
    account = Account.create()
    eth_address = account.address  # Account address derived from public key
    
    # Encode the message
    message = encode_defunct(text=m)
    
    # Sign the message using the account object
    signed_message = account.sign_message(message)
    
    # Return both the Ethereum address and the signature
    return eth_address, signed_message
