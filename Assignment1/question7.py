# Q7
# . Ask the user for a temperature in Celsius (string input). Convert it to float, 
# then calculate and print temperature in Fahrenheit

temperature=input("enter temperature in celsius: ")
temperature=float(temperature)
FahrenheitTemp=temperature*(9/5)+32
print("temperature in fahrenheit: ",FahrenheitTemp)