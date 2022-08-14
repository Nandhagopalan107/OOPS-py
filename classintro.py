from datetime import date
class Student:
    fees=20000
    no_of_student=0
    def __init__(self,name,id,dept,year,dob,city):
        self.name=name
        self.id=id
        self.dept=dept
        self.year=year
        self.dob=dob
        self.city=city
        Student.no_of_student+=1
        
    def address(self):
        add= f"Name : {self.name}\nDOB : {self.dob}\nID : {self.id}\ncity={self.city}"
        return add
    def age(self):
        curyear=date.today().year
        return curyear-self.dob
    def payfees(self,amt):
        self.fees= self.fees-amt
        
print("-----Getting student details-----")
Name=input("enter the name:")
Sid=input("enter the id:")
dept=input("enter the department:")
year=int(input("enter the year:"))
DOB=int(input("enter the DOB:"))
City=input("enter the city:")
stu1 = Student(Name,Sid,dept,year,DOB,City)
"""
#details display
print("Entered Student Detai;s are:")

print(stu1.address())
print("Age=",stu1.age(),end="")
print()"""

#claas-obj variables
stu1.payfees(10000)
stu2 = Student(Name,Sid,dept,year,DOB,City)
print(Student.fees)
print(stu1.fees)
print(Student.no_of_student)

    

