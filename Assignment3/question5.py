# Q5
# • 
# Keys = student names
# • 
# Values = marks (integer)
# A
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
# depending on the operation they want to perform on the dictionary:
# 1. - Add a student
# B
# 2. - Update marks
# C
# 3. - Search for a student
# D
# 4. - Display all students and marks


def Menu():
    print("A.Add a student")
    print("B.Update marks")
    print("C.Search for a student")
    print("D.Display all students names and marks")

students={
    "Kelash":60,
    "Aneel":80,
    "Sanjay":90
}

Menu()
ch=input("enter option:").upper()
match ch:
    case "A":
        name=input("Enter Name:")
        marks=int(input("Enter marks:"))
        students[name]=marks
    case "B":
        name=input("Enter name of student you want to update marks: ")
        if(students.get(name) is not None):
            marks=int(input("enter marks: "))
            students[name]=marks
        else:
            print("student does not exist in record")
    case "C":
            name=input("enter name of student: ")
            if(name in students):
                print(f"{name}:{students[name]}")
            else:
                print("student is not in record.")
    case "D":
             for name,marks in students.items():
                  print(name," : ",marks)
    case _:
        print("entered wrong input")
        

