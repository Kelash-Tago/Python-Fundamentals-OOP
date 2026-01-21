student={
    "name":"Kelash",
    "subjects":{
        "dld":50,
        "dsa":60,
        "se":70
    }
}

#key function
print(student.keys())

#value function
print(student.values())

#itmes
print(student.items())


#update method
newDic={
    "name":"Kumar"
}
student.update(newDic)
print(student) #name wil be updated

#I can write this also
student.update({"name":"Kelash Kumar"})
print(student)
