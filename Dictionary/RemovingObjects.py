student={
    "Name" : "Kelash",
    "Age"  :  20,
    "District": "Tharparkar"
}

student.pop("Age") #age became removed using key
print("After removing age: ",student)


# delete specific key
del student["District"]
print(student)

# for removing all items
student.clear()
print(student)