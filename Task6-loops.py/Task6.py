
# -----------------------for loop---------------------------------------


for i in range(1,4,1): #stop is skips the last one
    print("Hello World")

for i in range(2,17,3):
    print(i)

for i in range(3,0,-1):
    print(i)

for i in range(100,0,-10):
    print(i)

# sum of first 3 natural numbers

n=3
sum=0
for i in range(1,4,1):
    sum=sum+i
    # print(sum)
print(sum)   
sum=0
for i in range(1,4,1):
    sum=sum+10
print(sum)     

# sum of first 3 numbers

sum=0
sum=sum+1
sum=sum+2
sum=sum+3
print(sum)

# find the average of first n natural numbers using for loop

n=int(input("Enter a Number :"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
average=sum/n    
print(f"average of {n} natural number is = {average}")

# print the 2 table by using for loop

n=2
for i in range(1,11):
    mul=n*i
    print(f"multiplication of {n}*{i}={mul}")

n=3
for i in range(1,11):
    mul=i*n
    print(n,"*",i,"=",mul)    

# find the factorial of numbers

n=20
for i in range(1,n+1,1):
    if i%2==0:
        print(i)

s=15
n=11
for i in range(15,n-1,-1):
    if i%2!=0:
     print(i)

# write the code to display divisibles of 5 in the range of 5-10    

s=5
n=10
for i in range(5,11,1): #for i in range(s,n+1,1)
    if i%5==0:
     print(i) 

# count the even numbers in the range of 1 to 10

count=0
for i in range(1,11,1):
    if(i%2==0):
        count=count+1
print("Count of even numbers =",count)
    
#Display the sum of odd numbers in the range of 5-10  
sum=0
for i in range(5,11,1):
    if(i%2!=0):
        sum=sum+i
        # print("Sum of odd numbers =",sum)        

print("Sum of odd numbers =",sum)        

# Display the sum of odd numbers in the range of 15-5

sum=0
for i in range(15,4,-1):
    if(i%2!=0):
        sum=sum+i
print(sum)          

# write the code factors of 6(n or fact)

fact=6
for i in range(1,fact+1,1):
    if(fact%i==0):
        print(i)        
fact=8
for i in range(1,fact+1,1):
    if(fact%i==0):
        print(i)

# count the fators of given number

count=0
n=6
for i in range(1,n+1,1):
    if(n%i==0):
        count=count+1  #count+=1
print(count)

count=0
n=4
for i in range(1,n+1,1):
    if(n%i==0):
        count=count+1  #count+=1
print(count)
count=0
n=8
for i in range(1,n+1,1):
    if(n%i==0):
        count=count+1  #count+=1
print(count)

# counting a prime number/print the given number is prime number or not

prime=int(input("Enter a number :"))
count=0
for i in range(1,prime+1,1):
    if(prime%i==0):
      count=count+1  #count the prime number
# print("count =",count)
if(count==2):
      print(prime,"is a prime number") 
else :
   print(prime,"is not prime")       

# find the sum of factors of given number

fact=5
sum=0
fact=int(input("Enter a number :"))
for i in range(1,fact+1,1):
    if(fact%i==0):
        sum=sum+i
print("sum of factors =",sum)

# perfect number

n=6
sum=0
for i in range(1,n,1):
    if(n%i==0):
        sum=sum+i
# print(sum)
if(sum==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")    


# -----------------------------------While-Loop---------------------------------


#print 1 to 5 by using while loop
i=1
while(i<=5):
    print(i)
    i=i+1

# print the sequence of 0 5 10 15 20

i=0
while(i<=20):
    print(i)
    i=i+5

# print the sequence of 10 9 8 7 6 5

i=10
while(i>=5):
      print(i)
      i=i-1

# print the sequence of 9 6 3 0

i=9
while(i>=0):
    print(i)
    i=i-3

# write a code to display odd digit from given number

n=1234
while(n!=0):
    ld=n%10
    if(ld%2!=0):
        n//10    
print(ld)

# end

# print("Hello")
# print("Good Evening !")
print("Hello", end=" ") # "\n" is the default value
print("Good Evening !")        