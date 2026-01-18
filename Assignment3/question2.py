#average of all numbers in list
list=[13,45,34,66,45]

average=sum(list)/len(list)
print(average)



#we can manually calculate sum using loop as well
sum=0
for i in list:
    sum+=i
print("average : ",sum/len(list))

