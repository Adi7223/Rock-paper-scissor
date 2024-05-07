import random as r
user =int(input("for Rock press 0\nfor Paper press 1\nfor Scissor press 2 \n:"))
comp=r.randint(0,2)
if (user>2):
    print("invalid")
else: 
 print(f"the computer has chosen \n:{comp} ")

 if (comp==user):
    print("it's a draw")

 elif(comp==0 and user==1):
    print("you won")

 elif(comp==1 and user==2):
    print("you won")

 elif(comp==2 and user ==0):
    print("you won")

 else:
    print("you lose")

