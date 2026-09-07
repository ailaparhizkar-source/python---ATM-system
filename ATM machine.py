#ATM machine
mainPassword = "1234"
balance = 1000000
cardNum = "2346-2356-3456-6578"
aylaBalance = 2000000
###################################

print("WELCOME!")
passWord = input("password: ")
  

for i in range(3):
   if(passWord != mainPassword):
      passWord = input("password was wrong.Try again: ")
   
if(passWord == mainPassword):
   user = int(input("choose what you want to do:\n "
    "1.check balance\n2.cash withrawl\n3.money transfer\n"
    "4.change password\n5.EXIT\n"))
    
   if(user == 1):
     print(f"Your balance is {balance}")
   elif(user == 2):
    amount = int(input("Enter the amount: "))
    if(amount < balance):
      balance = balance - amount
      print(f"Cash withdrawl:{amount}\nYour balance now:{balance}")
    else:
      print("Insufficient fund!")
   elif(user == 3):
    amount = int(input("Enter the amount: "))
    card_num = str(input("Enter your Card number: "))
    if(amount > balance):
      print("Insufficient fund!") 

    elif(cardNum != card_num): 
         print("Invalid Card number!")
    else:
      balance = balance - amount
      aylaBalance = aylaBalance + amount
      print(f"Balance: {balance}\n Transfer amount:{amount}\nAyla's balance:{aylaBalance}")
   elif(user == 4):
    passW = str(input("Enter your old password: "))
    if(passW == mainPassword):  
      newPass = int(input("Enter your new password: "))
      newPass = int(input("Enter new password once more: "))
      print("Password successfully changed.")
    else:
      print("Password invalid!\ntry again.")
   elif(user == 5):
       print("Exit.")













