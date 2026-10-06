class Animal:
    def sleep(self):
        print("sleeping")
class cat(Animal):
    def meow(self):
        print("baby cat sounds meow")
c=cat()
c.meow()
c.sleep()
#######################################################################single inheritance with constructor without a super keyword##################################################################
class Person:
    def __init__(self, name):
        self.name = name
        print("Person Registered name as", self.name)

class Student(Person):
    def __init__(self, name, roll_number):
        Person.__init__(self, name)
        
        self.roll_number = roll_number
        print("Student Assigned Roll Number ",self.roll_number)

student1 = Student("Rahul", 25)
student2 = Student("maxy", 21)

########################################################################single inheritance with constructor with a super keyword ################################################################################

class School:
    def __init__(self, name, grade, address):
        self.name = name
        self.grade = grade
        self.address = address

class Student(School):
    def __init__(self, name, grade, address, stuname, student_id, course):
        super().__init__(name, grade, address)  # Passes school details to School class
        self.stuname = stuname
        self.student_id = student_id
        self.course = course

    def display(self):
        print(f"{self.stuname} is studying in {self.name}")
        print(f"Student ID is {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")
        print(f"School Address: {self.address}")

s = Student("Delhi Public School", "10th", "Hyderabad", "Bharath", 101, "Computer Science")
s.display()

############################## 2 SECOND EXAMPLE Single Inheritance — Constructor + super()##########################################################################
class Vehicle:
    def __init__(self):
        print("parent vehicle class")
        self.wheels = 4

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("car is toyota")
        self.color = "black"

    def display_details(self):
        print(f"car has {self.wheels} wheels")
        print(f"toyota {self.color} colored car")

c = Car()
c.display_details() 

############################## 3 THIRD EXAMPLE Single Inheritance — Constructor + super()##########################################################################
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        print("Bank account created")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate
        print("Savings account created")


account = SavingsAccount("ACC101", 6.5)

print(account.account_number)
print(account.interest_rate)

######################################################### MULTIPLE INHERITANCE WITHOUT CONSTRUCTOR##########################################
class Camera:
    def take_photo(self):
        print("taking a picture")
class Music:
    def play_music(self):
        print("playing music")
class Smartphone(Camera,Music):
    def make_call(self):
        print("calling")
s=Smartphone()
s.play_music()
s.take_photo()
s.make_call()

#############################################################MULTIPLE INHERITANCE WITH CONSTRUCTOR#############################################
class Employee:
    def __init__(self):
        print("Employee")
    def work(self):
        print("Employee is working")
class Developer:
    def __init__(self):
        print("Developer")
    def code(self):
        print("Developer is coding")
class SoftwareEngineer(Employee, Developer):
    def __init__(self):
        print("Software Engineer constructor")
engineer = SoftwareEngineer()
engineer.work()
engineer.code()

class Teacher:
    def __init__(self,subject):
        self.subject = subject
    def display_subject(self):
        print("Subject:",self.subject)
class Researcher:
    def __init__(self,research):
        self.research = research
    def display_research(self):
        print("Research Area:",self.research)
class Professor(Teacher,Researcher):
    def __init__(self,subject,research):
        Teacher.__init__(self,subject)
        Researcher.__init__(self,research)
        self.subject = subject
        self.research = research
p=Professor("python","Artificial Intelligence")
p.display_subject()
p.display_research()

#  MULTIPLE INHERITANCE WITHOUT CONSTRUCTOR


class Camera:
    def takePhoto(self):
        print("Camera is taking photo")


class MusicPlayer:
    def playMusic(self):
        print("Music is playing")


class Smartphone(Camera, MusicPlayer):
    def makeCall(self):
        print("Smartphone is making a call")


s = Smartphone()
s.takePhoto()
s.playMusic()
s.makeCall()


# 6. MULTIPLE INHERITANCE WITH CONSTRUCTOR
class Father:
    def __init__(self, father_name):
        self.father_name = father_name


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name


class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def display(self):
        print("Father Name:", self.father_name)
        print("Mother Name:", self.mother_name)
        print("Child Name:", self.child_name)


c = Child("Ramesh", "Sita", "Arjun")
c.display()

# 7. MULTIPLE INHERITANCE WITH CONSTRUCTOR + SUPER()


class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


class Tester(Employee):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool


class SoftwareEngineer(Developer, Tester):
    def __init__(self, name, language, tool):
        Developer.__init__(self, name, language)
        Tester.__init__(self, name, tool)

    def display(self):
        print("Employee Name:", self.name)
        print("Programming Language:", self.language)
        print("Testing Tool:", self.tool)


e = SoftwareEngineer("Kiran", "Python", "Selenium")
e.display()

# 8. MULTIPLE INHERITANCE WITH CONSTRUCTOR + SUPER()


class PersonalDetails:
    def __init__(self, name):
        self.name = name


class ContactDetails:
    def __init__(self, phone):
        self.phone = phone


class Customer(PersonalDetails, ContactDetails):
    def __init__(self, name, phone, address):
        PersonalDetails.__init__(self, name)
        ContactDetails.__init__(self, phone)
        self.address = address

    def display(self):
        print("Customer Name:", self.name)
        print("Phone Number:", self.phone)
        print("Address:", self.address)


c = Customer("Ganesh", "9876543210", "Visakhapatnam")
c.display()
inheritance.py