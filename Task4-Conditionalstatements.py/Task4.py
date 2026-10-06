# if block
# if True:
# if False:
#     print("If Block Executed")

# print("If Ended")    

# write a program to check whether a given number is equal to 10.
n=int(input("Enter a number :"))
n=int(input("Enter a number :"))
if n==10:
    print("True:Equal to 10")
print("end")    

# write a program which gives 15% discount if the billing price is greater than 5000 in in total bill.
# input=billing price
# process=logic billing>5000
# discount=15%
# output:billing price after discount

bp=6000
if bp>5000:
    discount=0.15*bp
    total_bill=bp-discount
    print("Bill =",bp)
    print("Bill after discount :",total_bill)

# if-else
# if False:
# if True:
#     print("True : If block Executed")
# else:
#     print("False : Else block Executed")    

n=int(input("Enter a number"))
if n==10:
    print("n= ",n, "is Equal to 10")
else:
    print("n =",n,"not equal to 10")

n=int(input("Enter a number :"))
if n<0:
    print("N is Negative")
else:
    print("N is positive")

# write a program to check the biggest number among two values

n1=int(input("Enter a number a:"))
n2=int(input("Enter a number b:"))
if n1>n2:
    print("n1 =",n1, "n1 is grater than n2 =",n2)
else:
    print("n1 =",n2, "n1 is grater than n1 =",n1)  

#write a program to check given number is even or not
num=int(input("Enter a number :"))
if num%2==0:
    print("num =", num, "num is even")
else:
    print("num =",num,"num is not even")   
 
# check the given number is odd or not

num=int(input("Enter a number :"))
if num%2!=0:
    print("num =", num, "num is odd")
else:
    print("num =",num,"num is even")    

# check given value is vowel or not

ch=input("Enter a Aphabet")
if ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" or ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("Alphabet is :", ch, "is vowel")
else:
    print("Alphabet is :", ch,"is not vowel")  

# check given value is alphabet or not

ch=input("Enter a value:")
if ch>="A" and ch<="Z" or ch>="a" and ch<="z":
    print("It is an Alphabet")
else:
    print("It is not Alphabet")  

# write a program to check given value is digit or not

n=int(input("Enter a digit:"))
# if n>="0" and n<="9":
if n>=0 and n<=9:
    print(n,"N is a digit")
else:
    print(n,"N is not a digit")  

# write a prgram name="hero" , psw=hero@123

name=input("Enter a name:")
psw=input("Enter a psw:")
if name=="hero" and psw=="hero@123":
    print("Login Successfull")
else:
    print("Invalid Credentials")    


# If-Elif-else-statements

# if(False):
#     print("Condition 1 is true:If block Executed")
# elif(False):
#     print("Condition 1 is false and con2 True: con2  elif is Executed")
# elif(False):
#     print("Condition 1 & 2 is false:cond3 elif is executed") 
# else:
#     print("All the above are false : Else block is executed")           

# check given num is positive negetive or zero
n=int(input("Enter a Number :"))
if(n>0):
    print("Positive Number")
elif(n<0):
    print("Negative Number")
else:
    print("Zero")        

# check given charecter is Alphabet ,digit or symbol

ch=input("Enter a Charecter :")
if (ch>="A" and ch<="Z" or ch>="a" and ch<="z"):
    print("Alphabet")
elif(ch>="0" and ch<="9"):
    print("digit") 
else:
    print("Symbol")   

# Display the grade based on given marks
# above 90 :O
# 71-90 : A
# 50-70 : B
# 35-50 : C
# below 35 : Fail 

marks=int(input("Enter a Grade :"))
if(marks>90):
    print("Grade : O")  
elif(marks>=71 and marks<=90):
    print("Grade : A")
elif(marks>=50 and marks<=70):
    print("Grade : B")
elif(marks>=35 and marks<=50):
    print("Grade : C")
else:
    print("Below 35: Fail")                   

# multiple If's

if(True):
    print("First If")
if(False):
    print("Second If")
if(True):
    print("Third If")   

# write a program to calculate the eletricity bill based on the units consumed

units=int(input("Enter a number of units consumed :"))
if(units<=100): 
    bill_amount=units*2  
    print("Total bill amount :",bill_amount)
elif(units<=200):
    bill_amount=units*4
    print("Total bill :",bill_amount)    
elif(units<=300):
    bill_amount=units*6
    print("Total bill :",bill_amount)
elif(units>300):
    bill_amount=units*8
    print("Total bill :",bill_amount)
else:
     print("Calculate the bill as per units")            

# write a program to check whether the given year is leap year or not

year=int(input("Enter a year :"))
if(year%400==0):
    print(year,"It is a leap year")
elif(year%4==0 and year%100!=0):
    print(year,"Is a leap year")  
else:
    print(year,"It is not a leap year")      


# Nested-if-Statements

if(True):
    print("Outer If Block")
    if(True):
        print("Inner If Block")
    else:
        print("Inner Else Block")
else:
    print("Outer Else Block")       

n=int(input("Enter a number :"))
if(n>0):
    print(n,"n is positive")
    if(n%2==0):
        print(n,"n is even")
    else:
        print(n,"n is odd")
else:
    print(n,"n is negetive") 

# display the smallest number from given two values only if they are not equal           

n1=int(input("Enter a Number :"))
n2=int(input("Enter a number :"))
if(n1!=n2):
    if(n1>n2):
        print(n2,"is smallest")
    else:
         print(n1,"is smallest")  
else:
    print("Both are equal")


# Match or switch statement

n=int(input("Enter a number :"))
match n:
    case 1:
        print("first case")
    case 2:
            print("second case")
    case 3:
            print("third case")            
    case _:
            print("default case")        

color=input("Enter a color :")

match (color):
    case "red":
      print("Stop vehicles and relax")
    case "orange":
      print("Start bike and get ready to go")  
    case "green":
      print("Go,Have a safe")  
    case _:
      print("Traffic Light Error")  

sides=int(input("Enter a side :"))
match sides:
    case 3:
      print("It is triangle")
    case 4:
      print("it is a square")  
    case 5:
      print("it is a pentagon")  
    case 6:
      print("it is a hexagon")  
    case _:
      print("Enter valid number")     

n=int(input("Enter a number :"))
match n:
    case 1:
      print("sunday")
    case 2:
      print("Monday")  
    case 3:
          print("Tuesday")  
    case 4:
          print("Thursday")           
    case 5:
          print("Friday") 
    case 6:
          print("Saturday")
    case _:
          print("Invalid")  

n1=int(input("Enter a number :"))
n2=int(input("Enter a number :"))
opr="-"
match opr:
    case "+":
        print("sum=",(n1+n2))          
    case "-":
            print("sub=",(n1-n2))          
    case "*":
            print("mul=",(n1*n2))          
    case "/":
            print("div=",(n1/n2))  
    case "%":
            print("rem=",(n1%n2))  
    case _:
                print("Invalid")                                                       


n1=int(input("Enter a number 1 :"))
n2=int(input("Enter a number 2 :"))
print("Select an option from the given choice")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Remainder")
option=int(input("Your Choice :"))
match option:
    case 1:
        print("Add",(n1+n2))
    case 2:
        print("Sub",(n1-n2))
    case 3:
            print("Mul",(n1*n2))
    case 4:
            print("Div",(n1/n2))
    case 5:
            print("Remainder",(n1%n2)) 
    case _:
            print("Invalid")    
     

# Restaurant Menu

print("----------Menu------------")
print("1.Biryani")
print("2.Chicken 65")
print("3.Veg Pulao")
print("4.Butter Chicken")
print("5.Chicken Lolipop")

menu=int(input("Enter your choice :"))
match menu:
    case 1:
        print("Item      :Biryani")
        print("Price     :   ₹100")
        print("Description:Spicy🔥 and Tasty")
    case 2:
            print("Item      :Chicken 65")
            print("Price     :   ₹150")
            print("Description:Spicy and Crispy😋")
    case 3:
            print("Item      :Veg Pulao")
            print("Price     :   ₹170")
            print("Description: Spicy🔥")
    case 4:
            print("Item      :Butter Chicken")
            print("Price     :   ₹200")
            print("Description:Yummy😋 and Tasty")
    case 5:
             print("Item      :chicken lolipop")
             print("Price     :   ₹250")
             print("Description:Crispy deepfry and Tasty☺️")
    case _:
            print("Sorry☹️ Not Available Now")


# ATM Menu  

print("-----------ATM Menu------------")
print("1.Check Balnce")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")

ATM=int(input("Enter your choice :"))

balance=50000

match ATM:
    case 1:
        print("Your balance is :",balance)
    case 2:
            deposite=int(input("Enter deposite amount :"))
            print("Your updated balance is :",deposite+balance)
    case 3:
            withdraw=int(input("Enter withdraw amount : "))
            print("Withdraw Successfull") 
            print("Remaining balance is",balance-withdraw)
    case 4:
            print("Thank you for visiting☺️")
    case _:
            print("Invalid!Try Again")


#Falsy values
 
if(""):
    print("Condition True:If Block Executed")
else:
    print("Condition False:Else Block Executed")    