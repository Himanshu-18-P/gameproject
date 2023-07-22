print("welcome to my game :) ")
a=input("you want to play??:  ")
if a.lower()!="yes":
    quit()
if a.lower()=='yes':
    print("okay!!")
import random as r
n=int(input("How many round you want to play: "))
for i in range(n):
    print("rock=0 , paper=1, scissors=2")
    a=int(input("enter a number: "))
    list_1=[0,1,2]
    c = r.choice(list_1)
    print(c) 
    if c==a:
       print("draw") 
    else:
        if a==1 and c==0 or a==2 and c==1 or a==0 and c==2:
           print("you win")
        else:
            print("computar win")
                 
    
            


        





