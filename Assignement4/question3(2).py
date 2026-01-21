# question in about a student class with private attributes and getter and setter methods
#with using property

class Student:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks
    @property
    def name(self):
        return self.__name
    @property
    def roll_no(self):
        return self.__roll_no
    @property
    def marks(self):
        return self.__marks
    @name.setter
    def name(self,name):
        if(name==""):
            print("Name can not be null")
        else:
            self.__name=name
    @roll_no.setter
    def set_roll_no(self,roll_no):
        if(roll_no>=1 and roll_no<=100):
            self.__roll_no=roll_no
        else:
            print("Roll Number should be between 1 and 100")
    @marks.setter
    def marks(self,marks):
        self.__marks=marks


student=Student("Kelash","023-24-0287",80)
student.name="Suneel"
#using property you can change variables easily and print easily
print(student.name)
