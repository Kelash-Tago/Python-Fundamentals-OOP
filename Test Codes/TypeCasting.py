#type casting from int to float and other data type or number to string
"""There are two types of type of casting
 1.explicit type casting (forcefully done by us )
 2.implicit type casting (automatically conversion like int to float )
"""
a=4
b=4.6
c="5"
#implicit conversion 
print(a+b) #her it will be 8.6 converted to float
print(type(a+b)) #type will be float 

#explicit conversion
print(type(int(c))) #here type will be int it is converted
print(3.3+int("2")) # answer will be 5.3
