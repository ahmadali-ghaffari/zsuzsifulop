# Create function that returns the name and balance of cash on an account
# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

accounts = [
    {'client_name': 'Igor', 'account_number': 111, 'balance': 10.5},
    {'client_name': 'Vladimir', 'account_number': 222, 'balance': 20.5},
    {'client_name': 'Sergei', 'account_number': 333, 'balance': 30}
]


account_from = int(input("Give me the bank account number to transfer!"))
account_to = int(input("Give me the bank account number to recive!"))
amount_to_transfer = float(input("Give me the amount!"))


def banking():
    something_goes_wrong = False
    if accounts[0]['account_number'] != account_from and accounts[1]['account_number'] != account_from and accounts[2]['account_number'] != account_from:  # nopep8
        print("404 - account not found for the transfer (account_from) ")
        something_goes_wrong = True
    elif accounts[0]['account_number'] != account_to and accounts[1]['account_number'] != account_to and accounts[2]['account_number'] != account_to:  # nopep8
        print("404 - account not found for the transfer (account_to) ")
        something_goes_wrong = True
    elif something_goes_wrong == False:
        for i in range(len(accounts)):
            if accounts[i]['account_number'] == account_from:
                if accounts[i]['balance'] >= amount_to_transfer:
                    new_balance = accounts[i]['balance'] - amount_to_transfer
                    print(new_balance)
        for j in range(len(accounts)):
            flag2 = False
            if accounts[j]['account_number'] == account_to:
                new_balance_2 = accounts[j]['balance'] + amount_to_transfer
                print(new_balance_2)


banking()
