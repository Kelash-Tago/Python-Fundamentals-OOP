# Q4
# "45"
# . The user enters a string containing a number (e.g., ). Convert it to:
# • 
# an integer
# • 
# a float
# • 
# a string again
# Print all three values with their types

value=input("enter value: ")
value=int(value)
print("integer number: ",value," type: ",type(value))
value=float(value)
print("float num: ",value," type: ",type(value))
value=str(value)
print("again to value ",value," type: ",type(value))