# 1. Display school details (without input and without return)
class School:
    @staticmethod
    def details():
        print("School : Sunrise High School")
        print("Location : Visakhapatnam")
        print("Board : CBSE")


School.details()
# -------------------------------------------------------------------------------------------------------------


# 2. Check whether a number is positive or negative (with input and without return)
class Number:
    @staticmethod
    def check(n):
        if n >= 0:
            print("Positive Number")
        else:
            print("Negative Number")


Number.check(-15)
# -------------------------------------------------------------------------------------------------------------


# 3. Return the number of hours in a day (without input and with return)
class Day:
    @staticmethod
    def get_hours():
        return 24


hours = Day.get_hours()
print("Hours in a day :", hours)
# -------------------------------------------------------------------------------------------------------------


# 4. Calculate the area of a square (with input and with return)
class Square:
    @staticmethod
    def area(side):
        return side * side


result = Square.area(8)
print("Area of square =", result)
# -------------------------------------------------------------------------------------------------------------


# Create a Bank class demonstrating all four types of static methods
class Bank:
    # 1. Without input and Without return
    @staticmethod
    def welcome():
        print("Welcome to ABC Bank")

    # 2. With input and Without return
    @staticmethod
    def check_balance(balance):
        if balance >= 5000:
            print("Sufficient Balance")
        else:
            print("Low Balance")

    # 3. Without input and With return
    @staticmethod
    def bank_name():
        return "ABC Bank"

    # 4. With input and With return
    @staticmethod
    def calculate_interest(amount):
        return amount * 5 / 100


Bank.welcome()
Bank.check_balance(8000)
name = Bank.bank_name()
print("Bank Name:", name)
interest = Bank.calculate_interest(10000)
print("Interest:", interest)


# 1. Display hospital details (without input and without return)
class Hospital:
    def details(self):
        print("Hospital : Apollo Hospital")
        print("Location : Hyderabad")
        print("Department : General Medicine")


h = Hospital()
h.details()
# -------------------------------------------------------------------------------------------------------------


# 2. Check whether a number is divisible by 5 (with input and without return)
class Number:
    def check(self, n):
        if n % 5 == 0:
            print("Divisible by 5")
        else:
            print("Not Divisible by 5")


n1 = Number()
n1.check(25)
# -------------------------------------------------------------------------------------------------------------


# 3. Return the number of days in a month (without input and with return)
class Month:
    def get_days(self):
        return 30


m = Month()
days = m.get_days()
print("Days in the month:", days)
# -------------------------------------------------------------------------------------------------------------


# 4. Find the square of a number (with input and with return)
class Number:
    def square(self, n):
        return n * n


n1 = Number()
result = n1.square(9)
print("Square of given number =", result)
# -------------------------------------------------------------------------------------------------------------


# Create a Student class demonstrating all four types of instance methods
class Student:
    # 1. Without input and Without return
    def welcome(self):
        print("Welcome to ABC College")

    # 2. With input and Without return
    def check_marks(self, marks):
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")

    # 3. Without input and With return
    def get_course(self):
        return "Python Full Stack"

    # 4. With input and With return
    def calculate_total(self, marks):
        return marks + 10


s1 = Student()
s1.welcome()
s1.check_marks(75)
course = s1.get_course()
print("Course:", course)
total = s1.calculate_total(80)
print("Total Marks:", total)