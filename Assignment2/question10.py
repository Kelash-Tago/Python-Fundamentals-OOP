#number guessing game
import random as r 

key=r.randint(1,100)
while True:
    num=int(input("enter number : "))
    if(num>key):
        print("Too High")
    elif num<key:
        print("Too low")
    else:
        print("correct!")
        break