#average of 3 numbers
# n1=int(input("Enter Num 1:"))
# n2=int(input("Enter Num 2:"))
# n3=int(input("Enter Num 3:"))
# sum=n1+n2+n3

# avg=sum/3
# print("average of",n1,n2,"and",n3,"=",avg)

#find the profit percentage by using selling price and cost price
# sp=int(input("Enter a selling price:")) #500
# cp=int(input("Enter Cost price")) #300 vbm./

# profit=sp-cp
# print("profit=",profit)
# profit_percentage=(profit/cp)*100
# print(profit_percentage,"%")

#find the missing angle in triangle by taking 2 angles

# angle1=int(input("Enter the angle 1:"))
# angle2=int(input("Enter The angle 2:"))
# sum=angle1+angle2
# angle3=180-sum
# print("Missing angle =",angle3,"degrees")

#find the last digit of given number
# a=int(input("Enter Num:"))
# b=a%10
# print("Last digit of given number:",a,"=",b)

#remove the last digit from the given number
# a=int(input("Enter a Number:"))
# b=a//10
# print("Remove the last digit from the given number:",a,"=",b)

# Find the first digit of 4 digit number
# n1=int(input("Enter a Number:"))
# b=n1//1000
# print("The First digit of 4 digit number:",n1,"=",b)

#find the sum of first n natural numbers
# n=int(input("Enter a Number:"))
# sum=n*(n+1)/2
# print("Sum of first n natural numbers:",n,"=",sum)

#find the average of first n natural numbers
# n=int(input("Enter a Number:"))
# avg=(n+1)/2
# print("Average of first n natural numbers:",n,"=",avg)

# Find the gross salary basic salary=20,000 bonus=20% incentives=5%
# basic=int(input("Enter a basic salary:"))
# bonus=int(input("Enter Bonus:"))
# incentive=int(input("Enter incentive:"))

# bonus=bonus/100*basic
# incentive=incentive/100*basic
# print("bonus =",bonus)
# print("incentive =",incentive)
# gross=basic+bonus+incentive
# print("Gross salary is",gross)

#find the inhand salary

# basic_sal=int(input("Enter basic sal:"))
# bonus=int(input("Enter bonus:"))
# incentive=int(input("Enter incentive:"))

# bonus=bonus/100*basic_sal
# incentive=incentive/100*basic_sal
# print("bonus",bonus)
# print("incentive",incentive)
# gross=basic_sal+bonus+incentive

# pf=int(input("Enter pf:"))
# health_ins=int(input("Enter health ins:"))

# pf=pf/100*basic_sal
# health_ins=health_ins/100*basic_sal
# inhand=gross-(pf+health_ins)
# print("Inhand salary is",inhand)

#swapping of two numbers using 3 variables

a=int(input("Enter a number"))
b=int(input("Enter b number"))
print("Before swapping")
print("a =",a)
print("b =",b)
c=a
a=b
b=c

print("After Swapping")
print("a =",a)
print("b =",b)

#swapping of 2 numbers by using two variables

a=int(input("Enter a number"))
b=int(input("Enter b number"))
print("Before swapping")
print("a =",a)
print("b =",b)
a=a+b
b=a-b
a=a-b
print("after swapping")
print("a =",a)
print("b =",b)

# Example-2

a=10
b=20
print("Before swapping")
print("a =",a)
print("b =",b)
a=a*b
b=a//b
a=a//b
print("after swapping")
print("a =",a)
print("b =",b)