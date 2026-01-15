#creation
details={
    "Name" : "Kelash",
    "Age"  :  20,
    "District": "Tharparkar"
}

#accessing
print(details)  #access all elements 

#access individual value
print("Name : ",details["Name"])

#more safe way for accessing individual element
print("Age : ",details.get("Age"))


# we can add tuples and lists in dictionary
enrollment={
    "Name":"Kelash",
    "Courses":["SE","DSA","DLD"]
}
print(enrollment)
