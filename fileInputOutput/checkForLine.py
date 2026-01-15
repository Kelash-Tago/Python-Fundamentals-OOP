
def checkForLine(str):
    data=True
    lineNo=1
    f=open("practice1.txt",'r')
    while data:
        data=f.readline()
        if(str in data):
            f.close()
            return lineNo
        else:
            lineNo+=1

    f.close()
    return -1

print(checkForLine("Python"))