from models import Account
from exceptions import (
    AccountNotFoundError,
    InsufficientFundsError,
    InvalidAmountError,
)


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_id = 1001

    def create_account(self, customer_name):
        account = Account(
            account_id=self.next_account_id,
            customer_name=customer_name,
            balance=0.0,
        )

        self.accounts[self.next_account_id] = account
        self.next_account_id += 1

        return account

    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account not found.")
        return self.accounts[account_id]

    def deposit(self, account_id, amount):
        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )

        account = self.get_account(account_id)
        account.balance += amount

    def withdraw(self, account_id, amount):
        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero."
            )

        account = self.get_account(account_id)

        if amount > account.balance:
            raise InsufficientFundsError("Insufficient balance.")

        account.balance -= amount

    def check_balance(self, account_id):
        account = self.get_account(account_id)
        return account.balance

    def close_account(self, account_id):
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account not found.")

        del self.accounts[account_id]