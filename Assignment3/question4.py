#Q4
# . Given a tuple of integers, create:
# • 
# A tuple of all even numbers
# • 
# A tuple of all odd numbers

numbers=(1,2,3,4,5,6,7,8)
oddNumbers=[]
evenNumbers=[]

for i in numbers:
    if(i%2==0):
        oddNumbers.append(i)
    else:
        evenNumbers.append(i)

oddNumbers=tuple(oddNumbers)
evenNumbers=tuple(evenNumbers)
print("odd numbers: ",oddNumbers)
print("even numbers: ",evenNumbers)
print(type(evenNumbers))