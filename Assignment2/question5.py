#sum of digits of number n

def sumOfDigits(n):
    sum=0
    while n!=0:
       sum+=n%10
       n=int(n/10)
       
    return sum

num=5348
print(f"sum of digits of {num} is {sumOfDigits(num)}")