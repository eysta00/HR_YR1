class Account(object):
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)
    
    def update_balance(self):
        self.balance *= self.intrest


class SavingsAccount(Account):
    intrest = 1.15
    def __init__(self, balance):
        Account.__init__(balance)

class DebitAccount(Account):
    intrest = 1.02
    def __init__(self, balance):
        Account.__init__(balance)


def update_accounts (accounts):
    for account in accounts:
        account.update_balance()

def print_accounts (accounts):
    for account in accounts:
        print(account)

s1 = SavingsAccount(1000)
d1 = DebitAccount(1000)
s2 = SavingsAccount(2000)
d2 = DebitAccount(4000)

accounts = [s1,d1,s2,d2]
print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)