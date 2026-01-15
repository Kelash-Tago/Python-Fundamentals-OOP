#packing of different datatypes in tuple
tup=("Kelash",20,"Python")
print("type of 0 index element : ",type(tup[0]))
print(tup)

# unpacking of tuple into variables
name,age,course=tup
print(name, " data type : ",type(name))
print(age, " data type : ",type(age))
print(course, "data type ",type(course))