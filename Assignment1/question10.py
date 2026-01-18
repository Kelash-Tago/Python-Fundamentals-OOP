# Q10
# 45.78
# . Take a decimal number as input (like  ) and output its:
# • 
# integer part - 
# 45
# • 
# fractional part - 
# .78

num=input("enter decimal number:")
integer_part,fractional_part=num.split(".")
print("integer part :",integer_part," fractional part ",fractional_part)