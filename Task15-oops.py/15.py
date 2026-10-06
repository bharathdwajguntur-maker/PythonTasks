# class person:
#     name="hero" #property
#     def talk(): #behaviour or action
#         print("Person is talking")
# person.talk()    


#1
# class student:
#     name="John"
#     def study():
#         print("Student is studying")
# student.study()

# class dog:
#     namee="Bruno"
#     def bark():
#         print("Dog is barking")
# dog.bark()

# class car:
#     name="Toyota"
#     def drive():
#         print("Car is driving")
# car.drive()

# class Teacher:
#     name="David"
#     def teach():
#         print("Teacher is teaching")
# Teacher.teach()        

# class mobile:
#     name="Samsung"
#     def call():
#         print("Mobile is ringing")
# mobile.call()


# class person:
#     #method
#     @staticmethod
#     # name="hero" #property
#     def talk(): #behaviour or action
#         print("I'm a static method")
# person.talk()    

# without input without return

# class Institute:
#     @staticmethod
#     def inst():
#         print("Name:Innomatics Research Lab")
# Institute.inst()        

# class Billing:
#     @staticmethod
#     def get_buill(amount,tax):
#         print("Total bill =",amount+tax)
# Billing.get_buill(1000,200)    

# class Bank:
#     @staticmethod
#     def bankName():
#         return "Innomatics bank"
# name=Bank.bankName()
# print("Name of the bank is",name)    

# Static Methods

# class Mathematicalopera:
# #without input without return add two numbers
#     @staticmethod
#     def add(a,b):    
#          a=10
#          b=20    
#          print("Addition of two numbers is",a+b)

# #with input without return sub two numbers
#     @staticmethod
#     def sub(n1,n2):
#         print("Substraction of two numbers is",n1-n2)

# #without input with return avg three numbers
#     @staticmethod
#     def division():
#           x=10
#           y=20
#           z=30
#           avg=(x+y+z)/3
#           return avg
#      # print("Average of three numbers is",avg)

# #with input with return mul of 4 numbers

#     @staticmethod
#     def mul(a,b,c,d):
#           return a*b*c*d
#      # print("Mul of numbers is",a*b*c*d)
# Mathematicalopera.add(10,20)       
# Mathematicalopera.sub(20,10)    
# print(Mathematicalopera.division())
# print(Mathematicalopera.mul(1,2,3,4))

# class palindrome:
#      def pali(self):
#           n=121
#           sum=0
#           while n!=0:
#                ld=n%10
#                sum=sum+10*ld
#                n=n//10
#           # print("Palindrome number")
# p1=palindrome()    
# p1.pali()    

# Instance Method

# class Test:
#      def myMethod(self):
#           print("I'm instance method")
# # Test.myMethod()
# t1=Test()
# t1.myMethod()

# #  with input without return

# class name:
#      def myName(self,name):
#           print("My name is ",name)
# n1=name()
# n1.myName("Janu")          

# Static Method

# class VariableEx:
#      name="Hero"
#      @staticmethod
#      def m1():
#       print("I am a static method name =",VariableEx.name)
#      @staticmethod
#      def m2():
#         print("I am a static method name =",VariableEx.name) 
# VariableEx.m1() 
# VariableEx.m2() 

# class Test:
#     name="Hero"
# class Abc:
#     @staticmethod
#     def m1():
#         print("M1 from abc here name =",Test.name)    
# Abc.m1() 

# @staticmethod
# def m2():
#      print("M1 from abc here name =",Test.name)      
# # Abc.m1()   
# Abc.m2()     
# t=Test()       
# t.m1()

# class Test:
#     def m1(self):
#         self.name="Zero"
#         print("I am a instance method m1 name =",self.name)
#     def m2(self):
#         print("I am a instance method m2 name =",self.name)
# t=Test()
# t.m1()        
# t.m2()

# class Test:
#     def m1(self):
#         self.name="Zero"
#         print("I am instance class name =",self.name)

# t=Test()
# t.m1()  
# class Result:
#     def res(self):
#         print("I am instance class result =",t.name)   
# a=Result()             
# a.res()      

#creating the instance variable by using object

# class Test:
#     def display(self):
#         print("My name is =",self.name)
#         print("Age is =",self.age)
#         print("Marks =",self.marks)
# t=Test()
# #name,age,marks
# t.name="Hero"
# t.age=21
# t.marks=80
# t.display()        

# class Student:
#     def displayDtails(self):
#         print("My name is =",self.name)
#         print("Age is =",self.age)
#         print("Marks =",self.course)
# stud1=Student()
# stud1.name="Hero"
# stud1.age=22
# stud1.course="Python"
# print("------Student1 Details------------")        
# stud1.displayDtails()

# stud2=Student()
# stud2.name="Zero"
# stud2.age=23
# stud2.course="Dot Net"
# print("------Student2 Details------------")        
# stud1.displayDtails()

# class Student:
    # ins_name="Innomatics" #static variable
# creating 
#     def assignData(self,name,age,course):
#         self.myName=name
#         self.age=age
#         self.course=course
#     def displayDetails(self):
#         print("Name",self.myName)
#         print("Age",self.age)
#         print("Course",self.course)
# s1=Student()
# print("------Student1 Details------------")   
# s1.assignData("Hero",21,"Python") 
# s1.displayDetails() 

# s2=Student()
# print("------Student2 Details------------")   
# s2.assignData("Hero2",22,"Java") 
# s2.displayDetails()   

# s3=Student()
# print("------Student3 Details------------")   
# s3.assignData("Hero3",23,"Dot net") 
# s3.displayDetails()   


# class employee:
        # company_Name="Infosys"
#     def empData(self,name,department,salary):
#         self.empName=name
#         self.empDepart=department
#         self.empSalary=salary
#     def displayempDetails(self):
#         print("Name of the Employe is ",self.empName)
#         print("Department of Employee is",self.empDepart)    
#         print("Salary of Employee",self.empSalary)
# e1=employee()        
# print("------------Employee1 Details---------------")
# e1.empData("Karthik","Teamlead",7500)
# e1.displayempDetails()

# e2=employee()        
# print("------------Employee2 Details---------------")
# e2.empData("Deepika","It",3500)
# e2.displayempDetails()

# e3=employee()        
# print("------------Employee3 Details---------------")
# e3.empData("Abhi","Production",2500)
# e3.displayempDetails()


class Teacher:
    clg_name="Narayana"
    def teacherData(self,name,subject,salary):
        self.techName=name
        self.techSubject=subject
        self.techSalary=salary
    def displayteachDetails(self):
        print("Name of the Teacher is ",self.clg_name)
        print("Name of the Teacher is ",self.techName)
        print("Department of Teacher is",self.techSubject)    
        print("Salary of Teacher",self.techSalary)
e1=Teacher()        
print("------------Teacher1 Details---------------")
e1.teacherData("Venu","Maths",7500)
e1.displayteachDetails()

e2=Teacher()        
print("------------Teacher2 Details---------------")
e2.teacherData("Venkatesh","Social",3500)
e2.displayteachDetails()

e3=Teacher()        
print("------------Teacher3 Details---------------")
e3.teacherData("Sowjanya","Science",2500)
e3.displayteachDetails()

class Movie:
    zoner="Classic"
    def movieData(self,name,price,rating):#class
        self.movieName=name
        self.moviePrice=price
        self.movieRating=rating
    def displayMoviedetails(self):
        print("Movie name is",self.movieName)
        print("Price of movie -",self.moviePrice)
        print("Rating -",self.movieRating)
m1=Movie()
print("---------------Movie Details-------------")
m1.movieData("Raja-Rani",100,8.5)
m1.displayMoviedetails()            

m2=Movie()
print("---------------Movie Details-------------")
m2.movieData("Hi Nana",150,9.0)
m2.displayMoviedetails()            