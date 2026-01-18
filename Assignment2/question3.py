# Q3
# . Write a function that prints the  
# n = 312
# digits
# n
# of a number, . 
# For eg:  , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [ 
# Hint- The right most digit of a number N is N%10. 
# And to remove the right most digit from a number, we can do N = N / 10.]


def printDigits(n):

    while n!=0:
       digit=n%10
       print(digit , end=" ")
       n=int(n/10)

num=1234
print("digits in  ",num,printDigits(num))
    