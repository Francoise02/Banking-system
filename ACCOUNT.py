#Create s class for Dangote bank account
class Account:
    # create a constructor
    def __init__(self, name="", client="", amount=0, account_number=""):
        self.name = name
        self.client = client
        self.amount = amount
        self.account_number = account_number

    print("Hello valued customer, You're welcome to Dangote bank!")

# create deposit method
    def deposit(self, clientaccounts):
        client_acc_name = input("Please enter your account name")
        if client_acc_name:
            for x in clientaccounts:
                if client_acc_name.lower() == x.name:
                    print(f"Welcome {client_acc_name}!")
                    deposit_amount = int(input("How much do you want to deposit?"))
                    x.amount = x.amount + deposit_amount
                    print(f"Hey {client_acc_name}, You have successfully deposited: {deposit_amount}, Your account balance is: {x.amount}")
                    stay = input('''Do you want do any other operation? reply by "yes" or "no"''')
                    if stay.lower() == "no":
                        print("Thank you, see you later!")
                        exit()
            if client_acc_name.lower() != x.name:
                print("Please enter a valid account name")

# Create a method to withdraw
    def withdraw(self, clientaccounts):
        client_acc_name = input("Please enter your account name")
        if client_acc_name:
            for x in clientaccounts:
                if client_acc_name.lower() == x.name:
                    print(f"Welcome {client_acc_name}!")
                    withdraw_amount = int(input("How much do you want to withdraw?"))
                    x.amount = x.amount - withdraw_amount
                    print(f"Hey {client_acc_name}, You have successfully withdrew: {withdraw_amount}, Your account balance is: {x.amount}")
                    stay = input('''Do you want do any other operation? reply by "yes" or "no"''')
                    if stay.lower() == "no":
                        print("Thank you, see you later!")
                        exit()
            if client_acc_name.lower() != x.name:
                print("Please enter a valid account name")

# Create a method to check the account balance
    def balance(self, clientaccounts):
        client_acc_name = input("Please enter your account name")
        if client_acc_name:
            for x in clientaccounts:
                if client_acc_name.lower() == x.name:
                    print(f"Hello {client_acc_name},")
                    print(f"Your account balance is: {x.amount}")
                    stay = input('''Do you want do any other operation? reply by "yes" or "no"''')
                    if stay.lower() == "no":
                        print("Thank you, see you later!")
                        exit()
            if client_acc_name.lower() != x.name:
                print("Please enter a valid account name")

# Create a method to transfer money between accounts
    def transfer(self, clientaccounts):
        sender = input("Enter your account name")
        if sender:
            for x in clientaccounts:
                if sender.lower() == x.name:
                    print(f"Hello {x.name}, you're welcome!")
                    receiver = input("Please enter receiver's account name?")
                    if receiver:
                        for i in clientaccounts:
                            if receiver.lower() == i.name:
                                money = int(input(f"How much do you want to send to {receiver}? "))
                                if i.amount < money:
                                    print("Insufficient balance!")
                                else:
                                    x.amount = x.amount - money
                                    i.amount = i.amount + money
                                    print(f"Hey {x.name}, You have successfully transferred: {money} to {i.name}, your account balance is: {x.amount}")
                                    stay = input('''Do you want do any other operation? reply by "yes" or "no"''')
                                    if stay.lower() == "no":
                                        print("Thank you, see you later!")
                                        exit()
                        if sender.lower() != x.name:
                            print("Please enter a valid account name")
            if sender.lower() != x.name:
                print("Please enter a valid account name")

# Create a method to view client accounts
    def view(self, clientaccounts):
        accno = 0
        for x in clientaccounts:
            accno = accno + 1
            print("\nACCOUNT " , accno , "\n-----------")
            print("Account name:", x.name)
            print("Client's name:", x.client)
            print("Account balance:", x.amount)
            print("Account number:", x.account_number)

        stay = input('''Do you want do any other operation? reply by "yes" or "no"''')
        if stay.lower() == "no":
            print("Thank you, see you later!")
            exit()
