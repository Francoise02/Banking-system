# Importing the Bank account class
from ACCOUNT import Account

from CURRENT import Current_Acc

from SAVING import Saving_Acc

# Creating accounts collection
clientaccounts = []

# Inserting existing accounts
clientaccounts.append(Account("francoise", "Mukantwari Francoise", 700000, "012345678"))
clientaccounts.append(Account("binusha", "Binusha Balachandran", 500000, "012345677"))
clientaccounts.append(Account("lolita", "Lolita had", 100000, "012345676"))
clientaccounts.append(Account("fils", "Fils Noel", 103000, "012345675"))
clientaccounts.append(Account("clare", "Clare Kanja", 210000, "012345674"))
clientaccounts.append(Account("natasha", "Natasha Mramba", 490000, "012345673"))
clientaccounts.append(Account("derrick", "Derrick Odonkor", 90000, "012345672"))
clientaccounts.append(Account("david", "David Mugisha", 350000, "012345671"))

# Ask the user the account they want to use
account_type = int(input('''Which account type do you use?
 1. Current account, enter 1
 2. Saving account, enter 2'''))

# Output for current account
if account_type == 1:
    operation = int(input('''Which operation do you want to make?
    1. Deposit, enter 1
    2. Withdraw, enter 2
    3. Transfer money to another account, enter 3'''))
    if operation == 1:
        current_deposit = Current_Acc()
        current_deposit.deposit(clientaccounts)
    if operation == 2:
        current_withdraw = Current_Acc()
        current_withdraw.withdraw(clientaccounts)
    if operation == 3:
        current_transfer = Current_Acc()
        current_transfer.transfer(clientaccounts)

# Output for saving account
if account_type == 2:
    operation = int(input('''Which operation do you want to do?
        1. Deposit, enter 1
        2. Withdraw, enter 2
        3. Transfer money to another account, enter 3'''))
    if operation == 1:
        saving_deposit = Saving_Acc()
        saving_deposit.deposit(clientaccounts)
    if operation == 2:
        saving_withdraw = Saving_Acc()
        saving_withdraw.withdraw(clientaccounts)
    if operation == 3:
        saving_transfer = Saving_Acc()
        saving_transfer.transfer(clientaccounts)


