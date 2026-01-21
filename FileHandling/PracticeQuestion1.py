# f=open("practice1.txt","a+")
# f.write("Hi everyone \nwe are learning file I/O\nusing Java.\nI like programming in Java.")


with open("practice1.txt","r") as f:
    data=f.read()
    newData=data.replace("Java","Python")
    print(newData)

#now overwriting on file
with open("practice1.txt","w") as f:
    data=f.write(newData)

#now find learning exists or not in data
word = "learning"
with open("practice1.txt","r") as f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("Not found")

