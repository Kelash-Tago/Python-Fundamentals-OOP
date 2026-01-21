from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
     def calculate_salary(self):
         return 30000
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
    
class ContractEmployee(Employee):
    def calculate_salary(self):
        return 70000

#print salaries 

employees=[
    Intern(),FullTimeEmployee(),ContractEmployee()
]
for employee in employees:
    print("Salary: ",employee.calculate_salary())
