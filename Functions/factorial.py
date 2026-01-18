def factorial(num):
    factNum=1
    for i in range(1,num+1):
        factNum*=i

    return factNum

print(factorial(5))