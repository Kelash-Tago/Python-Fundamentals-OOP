# Q8 Write a program to check whether two lists share no common elements. 

list1=[1,2,3,4]
list2=[3,4,5,6]

list1=set(list1)
list2=set(list2)
print("common elements: ",list1.intersection(list2))