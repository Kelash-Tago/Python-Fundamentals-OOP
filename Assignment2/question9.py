#check number is prime or not 

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
num=int(input("enter number: "))
print("Prime:",isPrime(num))