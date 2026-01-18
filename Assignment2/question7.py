# Q7
# . Design a program to continuously input a number n  from user & print if it is 
# positive or negative until the user enters “Quit”
while True:
    
    word=input("enter number: ")
    if(word=="Quit"):
        break
   
    if not word.strip().isdigit():
        continue

    num=int(word)
    if(num>=0):
        print("positve")
    else:
        print("negative")
    