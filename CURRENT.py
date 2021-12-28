# Importing Account class from ACCOUNT file
from ACCOUNT import Account


# Create saving class with a method to withdraw
class Current_Acc(Account):
    def withdraw(self, clientaccounts):
        withdrawer_name = input("Please enter your account name")
        if withdrawer_name:
            for x in clientaccounts:
                if withdrawer_name.lower() == x.name:
                    withdraw_amount = int(input("How much do you want to withdraw?"))
                    x.amount = x.amount - withdraw_amount
                    a = int(input("How many months did the money stay the the account?"))
                    if a >= 1:
                        interest = withdraw_amount * (1/100)
                        print(f"Since your money has stayed in your account for more than a month,"
                              f"You will get an interest of 1% that is: {interest},"
                              f"Your account balance is; {x.amount + interest}")
                        print(f'Thank you {withdrawer_name}, see you later!')
                    else:
                        print(f"Your account balance is: {x.amount}")

