accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account
# def balance_client(accounts):
#     for i in range(len(accounts)):
#         print (accounts[i]['client_name'] +" " + str(accounts[i]['balance']))
# balance_client(accounts)


# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

#from=f
#to=t
#amount=a
f = 11234543
t = 43546731
a = 203004099.2

#ez a függvény megtalálja az f változóban tárolt számlát és levonja róla a összeget amit utalni szeretnénk

def f_from(f, t, a):
    for i in range(len(accounts)):
        if (accounts[i]['account_number']) == f:
            rest_of_money = accounts[i]['balance'] - a
            print("Hey, I found the account", accounts[i]['account_number'], 'the old balance was', accounts[i]['balance'], 'the new balance is:', rest_of_money)
    if (accounts[i]['account_number']) != f:
        print("404 - account not found")
        return
        
f_from(f, t, a)

def t_to(f, t, a):
    for i in range(len(accounts)):
        if (accounts[i]['account_number']) == t:
            new_money = accounts[i]['balance'] + a
            print("Hey, I found the account", accounts[i]['account_number'], 'the old balance was', accounts[i]['balance'], 'the new balance is:', new_money)
    if (accounts[i]['account_number']) != t:
        print("404! - account not found")
        return
t_to(f, t, a)
