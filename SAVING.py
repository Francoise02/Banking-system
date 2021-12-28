# Importing Account class from ACCOUNT file
from ACCOUNT import Account

# Create saving class with a method to withdraw
class Saving_Acc(Account):
    def withdraw(self, clientaccounts):
        withdrawer_name = input("Please enter your account name")
        if withdrawer_name:
            for x in clientaccounts:
                if withdrawer_name.lower() == x.name:
                    print(f'Your welcome {withdrawer_name}')
                    a = int(input("How many months did the money stay the the account?"))
                    if a >= 6:
                        withdraw_amount = int(input("How much money do you want to withdraw?"))
                        x.amount = x.amount - withdraw_amount
                        interest = withdraw_amount * (3 / 100)
                        print(f"Since your money has stayed in your account for more than 6 months,"
                              f" you will get an interest of 3% that is: {interest}, "
                              f"Your account balance is: {x.amount + interest}")
                        print(f'Thank you {withdrawer_name}, see you later!')
                    else:
                        print("Please note that you cannot withdraw, wait until you reach 6 months")

