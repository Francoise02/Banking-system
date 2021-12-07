# Importing the class
from ACCOUNT import Account

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
loop = True
while(loop):
    # Ask the user operation they want to make
    operation = input('''Which operation do you want to do?
    1. Deposit, enter 1
    2. Withdraw, enter 2
    3. Check your account balance, enter 3
    4. Transfer money to another account, enter 4
    5. If you would like to view our client accounts before you test the code, enter 5''')
    if operation == "1":
        deposit = Account()
        deposit.deposit(clientaccounts)
    elif operation == "2":
        withdraw = Account()
        withdraw.withdraw(clientaccounts)
    elif operation == "3":
        check = Account()
        check.balance(clientaccounts)
    elif operation == "4":
        transfer = Account()
        transfer.transfer(clientaccounts)
    elif operation == "5":
        view = Account()
        view.view(clientaccounts)
