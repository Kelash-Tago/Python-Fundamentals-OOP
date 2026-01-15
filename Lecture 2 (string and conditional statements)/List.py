list=[2,3,4]
print(list)

#we can change index
list[1]=5
list.append(7) #add element in last
print(list)
list.sort() #sort list is ascending order
print(list)
list.sort(reverse=True) #sort list in descending order
print(list)
#note sorting is possible in string elements 

# add element at specific index
list.insert(1,9)
print(list)

#remove fuction it removes first occurrence'
list=[1,2,3,4,5]
list.remove(3)
print("after removing first occurrence of 3 : ", list)
list.pop()
print("after calling pop ",list)
list.pop(0)
print("after calling pop(0)",list)

list=["kelash",3,True] #we can add multiple data types
print(list)
print("type of first index is : ",type(list[0]))