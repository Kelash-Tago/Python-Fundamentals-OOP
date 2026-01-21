# question in about a student class with private attributes and getter and setter methods

class Student:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks
    def set_name(self,name):
        if(name==""):
            print("Name can not be null")
        else:
            self.__name=name
    def set_roll_no(self,roll_no):
        if(roll_no>=1 and roll_no<=100):
            self.__roll_no=roll_no
        else:
            print("Roll Number should be between 1 and 100")
    def set_marks(self,marks):
        self.__marks=marks


student=Student("Kelash","023-24-0287",80)
print(f"Name: {student.get_name()} \nRoll Number: {student.get_roll_no()} \nMarks: {student.get_marks()}")
    
# here this will create a new instance variable not overwriting existing  private variable 
student.__name="Sanjay"
print(student.__name)
print(student.get_name()) #it will still print Kelash

    
    