list=[1,3,5,7,8]
def PrintListLength(list):
    length=0
    for i in range(0,len(list)):
        length+=1
    return length    

print(PrintListLength(list))

def printList(list):
    for i in range(0,len(list)):
        print(list[i])
printList(list)