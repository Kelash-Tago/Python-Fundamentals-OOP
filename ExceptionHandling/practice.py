try:
   num=10
   a=int(input("enter number : "))
   ans=num/a
except ZeroDivisionError:
    print("divide by zero is not allowed")
except ValueError:
    print("enterd wrong value.")
else:
     print(f"ans: {ans}")
finally:
     print("must be executed..")