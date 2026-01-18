# Q7 Write a program that takes a string from the user and prints the number of 
# spaces in the string

string=input("enter a string: ")
count=0
for ch in string:
    if(ch==" "):
        count+=1

print("Spaces in string: ",count)

# we can do with built in method as well
print("Spaces in string ",string.count(" "))
