str ="Kelash"
print(str[1]) #it will print e
 # this will print all characters using loop
for i in str:
    print(i)


str="Kelash Kumar from Tharparkar"
print("Kumar" in str )# prints True it is case sensitive

print("suneel " not in str) #True
# we can use these in if statements
if "from" in str:
      print("yes from is in the string")