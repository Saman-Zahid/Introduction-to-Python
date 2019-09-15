#question 1

import datetime # we will use this for date objects
class Person:
    instances = []
    
    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        Person.instances.append(self)

        

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self._age = age        
        return age
     
    @classmethod
    def get_persons(cls):
        return(list(cls.instances))
        
    @classmethod
    def persons_created(cls):
        return(len(cls.instances))
    
    def get_id(self):
        raise NotImplementedError("To be implemented")
        
        
# Test code:

# 1.1
p1 = Person("Anna", "Annasdotter", datetime.date(1975, 4, 4))
print(p1.get_age())

# 1.2
p2 = Person("Sven", "Svensson", datetime.date(1978, 5, 5))
print(p1.persons_created())
print(Person.persons_created())
pers = p1.get_persons()
print(pers)

# 1.3
#print(p1.get_id())
    


#question 2 
# Your class definitions here:

from random import randint
import datetime

class Employee(Person):
    instances = []
    
    def __init__(self,name,surname,birthday,salary = 0):
        super(Employee,self).__init__(name,surname,birthday)
        #Person.__init__(self,name,surname,birthday)
        self.salary = salary
        self.id = "{0}{1}{2}".format(self.name[0:3].lower(),self.surname[0:3].lower(),Employee.random_number())
        Employee.instances.append(self)
    
    @classmethod
    def random_number(cls,n=2):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    
    
    def get_id(self):
        return(self.id)
    
    @classmethod
    def employees_created(cls):
        return(len(cls.instances))
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self,salary):
        self.salary = salary
    
class Student(Person):
    
    instances = []
    
    def __init__(self,name,surname,birthday,course=""):
        super(Student,self).__init__(name,surname,birthday)
        #Person.__init__(self,name,surname,birthday)
        self.id = "{0}{1}{2}".format(self.name[0:3].lower(),self.surname[0:3].lower(),Student.random_number())
        
        self.program = course
        Student.instances.append(self)
        
    
    @classmethod
    def random_number(cls,n=3):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    
    
    def get_id(self):
        return(self.id)
    
    @classmethod
    def students_created(cls):
        return(len(cls.instances))
    
    def get_program(self):
        return self.program
    
    def set_program(self,program):
        self.program = program
        
    
# 2.1
e1 = Employee("Anders", "Andersson", datetime.date(1960, 1, 1))
print(e1.get_id())
print(e1.get_id())
s1 = Student("Peter", "Petersson", datetime.date(1990, 2, 2))
print(s1.get_id())
print(s1.get_id())
print("\n")
# Your test code for 2.2:
print("Total Person {0}".format(Person.persons_created()))
print("Total student {0}".format(Student.students_created()))
print("Total employee {0}".format(Employee.employees_created()))
print("\n")

# 2.3
s1 = Student("Peter", "Petersson", datetime.date(1990, 2, 2), "Statistics")
print(s1.get_id())
print(s1.get_id())


# 2.4
e1 = Employee("Anders", "Andersson", datetime.date(1960, 1, 1), 40000)
print(e1.get_id())
print(e1.get_id())







#question 3
class PhDStudent(Student,Employee):
    
    def __init__(self,name,surname,birthday,program="",salary=0):
        
        super(PhDStudent,self).__init__(name,surname,birthday,salary)
        super(PhDStudent,self).__init__(name,surname,birthday,program)
        #super(PhDStudent,self).__init__(name,surname,birthday,salary)
      #  Student.__init__(self,name,surname,birthday,program)
       # Employee.__init__(self,name,surname,birthday,salary)
        
        #self.id = self.id = "{0}{1}{2}".format(self.name[0:3].lower(),self.surname[0:3].lower(),Employee.random_number())
        


# Test code:
# 3.1
class PhDStudent(Student,Employee):
    
    def __init__(self,name,surname,birthday,program="",salary=0):
        
        super(PhDStudent,self).__init__(name,surname,birthday,salary)
        super(PhDStudent,self).__init__(name,surname,birthday,program)
        #super(PhDStudent,self).__init__(name,surname,birthday,salary)
      #  Student.__init__(self,name,surname,birthday,program)
       # Employee.__init__(self,name,surname,birthday,salary)
        
        #self.id = self.id = "{0}{1}{2}".format(self.name[0:3].lower(),self.surname[0:3].lower(),Employee.random_number())
        


# Test code:
# 3.1
phd1 = PhDStudent("Elin", "Elinsdotter", datetime.date(1980,3,3), "Machine Learning", 30000)
print(Person.persons_created())
print(Employee.employees_created())
print(Student.students_created())
print(phd1.get_id())
print(phd1.get_salary())
print(phd1.get_program())("Elin", "Elinsdotter", datetime.date(1980,3,3), "Machine Learning", 30000)
print(Person.persons_created())
print(Employee.employees_created())
print(Student.students_created())
print(phd1.get_id())
print(phd1.get_salary())
print(phd1.get_program())


PhDStudent("Elin", "Elinsdotter", datetime.date(1980,3,3))
