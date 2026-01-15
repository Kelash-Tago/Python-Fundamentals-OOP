# (a) Using parentheses:
tup=(2,3,5,6,6)
print(tup)

#(b) Without parentheses (tuple packing):
tup=1,2,3
print(tup)

#c) Single element tuple (important!):
tup=(1)
print(tup)
print(type(tup)) # it is integer not a tuple
# for single element if we are making tuple so we have to add comma
tup=(1,)
print(tup)
print(type(tup)) # here it is tuple
# or we can write like this
tup=1,
print(tup)
print(type(tup))