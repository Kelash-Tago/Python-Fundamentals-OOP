# Given a list, print all elements that appear more than once in the list.

numbers=[1,2,3,3,4,4,4,5,6,7,8,9,9]
set1=set()
set2=set()
for num in numbers:
    if(num in set1):
       set2.add(num)
    else:
        set1.add(num)
print("duplicate elements: ",set2)