import re


class TransferError(Exception):
    pass

def transfer(from_account, to_account, amount, balance):
    account_pattern = r"^\d{10}$"
    
    if not re.match(account_pattern, from_account) or not re.match(account_pattern, to_account):
        raise TransferError("invalid account number format")

    if amount <= 0:
        raise TransferError("transfer amount must be greater than zero")
    if amount>balance:
        raise TransferError("insufficient balance for transfer")
    
    return True