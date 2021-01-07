print("Welcome to Chase bank.")



new_balance = True
data = "Have a nice day!"
print(data)
def bank(data):
    data = str(input("What would you like to do? "))
    new_balance = True
    if new_balance == True:
        balance = 4000
    if data == 'deposit':
        deposit = int(input('How much would you like to deposit? '))
        message ='Your balance is {}'
        print(message.format(balance + deposit))
        balance = balance + deposit
        new_balance = False
    elif data == 'withdraw':
        withdraw = int(input('How much would you like to withdraw? '))
        message ='Your balance is {}'
        print(message.format(balance - withdraw))
        balance = balance - withdraw 
        new_balance = False
    else: print(balance) 
    new_balance = false
    data1 = str(input("Are you done? "))
    if data1 =="yes":
        print('Thank you!')
    else: return bank(data)   
    

bank(data)



    
 


    