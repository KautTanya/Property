"""Account"""


class Account:
    """Account"""
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self._account_holder = account_holder

    @property
    def balance(self):
        """balance"""
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value
        else:
            print("Balance must be greater than 0.")

    @property
    def account_holder(self):
        """account_holder"""
        return self._account_holder


account = Account(1000, "Jack")

print(account.balance)
print(account.account_holder)

account.balance = 0
print(account.balance)