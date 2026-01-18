word="Kelash"
#i can print index individually
print(word[1])

#strings are immutable so you can not change its index
# word[1]='a'    shows error

# slicing
print("slicing in string")
print(word[:3])
print(word[1:])
print(word[-4:-1])

# methods 
print("length of the word is :",len(word))
word="  Kelash     "
print(f"without removing spaces {word} after removal {word.strip()}")
print("in lower case: ",word.lower())


# concatenation
firstName="Kelash"
lastName="Kumar"
print(firstName+" "+lastName)

#format method
a=1
b=2
sum=a+b
print("sum of {1} and {0} is {2}".format(a,b,sum))

# f string is better choice 
print(f"sum of {a} and {b} is {sum}")