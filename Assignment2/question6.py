# 1 to 100 numbers dividable by three and five

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i,end=" ")
    i+=1
