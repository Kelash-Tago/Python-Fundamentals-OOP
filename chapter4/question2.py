list=[]
for i in range(7):
    num=int(input(f"enter marks of student   {i+1} :"))
    list.append(num)

print(list)
list.sort()
print(f"list in sorted order : {list} ")
