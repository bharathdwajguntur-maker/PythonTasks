# class Test:
#    #instance method
#    #parametarized constructor
#    def __init__(self,myName,age):
#     #   print("I am a constructor")
#     print("My name is = ",myName)
#     print("Age = ",age)
# t1=Test("Constructor",20)      

# class Test:
#    #instance method
#    #parametarized constructor
#    def __init__(self,myName):
#     #   print("I am a constructor")
#          return None
# t1=Test("Constructor")
# print(t1) #error        

# class Student:
#      ins_name="Fullstack Ecadamy"
#      #creating instance variable
#      def __init__(self,name,age,course):
#           self.myName=name
#           self.myAge=age
#           self.myCourse=course
#      def displayDetails(self):     
#           print("Name is =",self.myName)
#           print("Age is =",self.myAge)
#           print("Course is =",self.myCourse)
#           print("Student Institute name is =",self.ins_name)

# s1=Student("Radha",21,"Python")
# print("----Stu1 Details--------")
# s1.displayDetails()

# s2=Student("Sudha",22,"Java")
# print("----Stu2 Details--------")
# s2.displayDetails()

          
# class Bank:
#      bank_Name="SBI"
#      bank_location="Hyderabad"
#      #creating instance variable
#      def __init__(self,customer_Name,customer_acNo,ac_Balance,ac_type):
#           self.customer_Name=customer_Name
#           self.customer_acNo=customer_acNo
#           self.ac_Balance=ac_Balance
#           self.ac_type=ac_type

#      def bankDetails(self):     
#           print("Name of the Bank",self.bank_Name)
#           print("Student Institute name is ",self.bank_location)
#           print("Name of the Customer is",self.customer_Name)
#           print("Account number of customer is",self.customer_acNo)
#           print("Remaining bank Balance",self.ac_Balance)
#           print("Type of bank is ",self.ac_type)

# b1=Bank("Radha",12345671,5000,"Savings")
# print("----customer1 Details--------")
# b1.bankDetails()

# b2=Bank("Sudha",22340987654,3000,"Current")
# print("----customer2 Details--------")
# b2.bankDetails()

# class Teacher:
#     clg_name="Narayana"
#     pincode=12345
#     def __init__(self,name,subject,salary,location):
#         self.techName=name
#         self.techSubject=subject
#         self.techSalary=salary
#         self.techlocation=location
#     def displayteachDetails(self):
#         print("Name of the College is ",self.clg_name)
#         print("Name of the Teacher is ",self.techName)
#         print("Department of Teacher is",self.techSubject)    
#         print("Salary of Teacher",self.techSalary)
#         print("Location of the teacher is",self.techlocation)
#         print("College pincode is",self.pincode)
# t1=Teacher("Venu","Maths",7500,"Ameerpet")        
# print("------------Teacher1 Details---------------")
# t1.displayteachDetails()

# t2=Teacher("Venkatesh","Social",3500,"JNTU")        
# print("------------Teacher2 Details---------------")
# t2.displayteachDetails()

# t3=Teacher("Sowjanya","Science",2500,"KBHP")        
# print("------------Teacher3 Details---------------")
# t3.displayteachDetails()

# class employee:
#     company_Name="Deloitte"
#     company_location="Banglore"
#     def __init__(self,id,name,department,salary):
#         self.id=id
#         self.empName=name
#         self.empDepart=department
#         self.empSalary=salary
#     def displayempDetails(self):
#         print("Name of the Company is ",self.company_Name)
#         print("Location of the Company is ",self.company_location)
#         print("Name of the Employe is ",self.empName)
#         print("Department of Employee is",self.empDepart)    
#         print("Salary of Employee",self.empSalary)
# e1=employee(1,"Karthik","Teamlead",7500)        
# print("------------Employee1 Details---------------")
# e1.displayempDetails()

# e2=employee(2,"Deepika","It",3500)        
# print("------------Employee2 Details---------------")
# e2.displayempDetails()

# e3=employee(3,"Abhi","Production",2500)        
# print("------------Employee3 Details---------------")
# e3.displayempDetails()


#---------------------------------Destructor------------------------

# class Student:
#     def __init__(self):
#         print("Object is created :Constructor is invoked")
#     def __del__(self):
#         print("Object is going to destroyed : Destructor is invoked") 
# s1=Student()
# # print("We gonna delete object ---Manually")
# # del s1
# print("Program ended")   


#-----------------------------------------Class Method-------------------------

# class Student:
#     institute="Innomatics"
#     @classmethod
#     def m1(cls):
#         print("Institute in class method",cls.institute)
#     @staticmethod
#     def m2():
#         print("I am a static Mthod",Student.institute)
# #invoke
# Student.m1()
# Student.m2()                     


# class Student:
#     institute="FullStack"
#     def m1(self):
#         self.name="Hero"
#         print("Static variable",self.institute)
#         print("Instance variable",self.name)
#     @classmethod
#     def m2(cls):
#         print("I am a class Method(Static variable)",cls.institute)
#         print("Instance variable",cls.name)  #wrong dont work
# #invoke
# Student.m1()
# Student.m2()                     