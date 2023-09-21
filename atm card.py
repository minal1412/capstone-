cardno=int(input("Enter the card number"))
if cardno == 12345 or cardno == 67890:
 print("welcome",cardno)
 pin=input("enter pin number")
 if pin=="0000":
   print("acces granted")
   amount=int(input("enter amount to withdraw"))
   balance=10000
   if amount > balance:
     print("insuffiecient balance")
   else:
     print("take cash",amount)
     print(balance - amount,"is the available balance")
 else:
   print("incorrct pin")
else:
 print("invalid card")

