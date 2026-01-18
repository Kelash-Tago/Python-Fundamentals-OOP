# 1. Print multiplication table for any number 
#      . [using  while loop ] 

num=int(input("enter table number : "))
i=1
while i<=10:
    print(f"{i} * {num}= {i*num}")
    i+=1