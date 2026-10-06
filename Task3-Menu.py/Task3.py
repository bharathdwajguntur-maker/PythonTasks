print("----MENU-----")
print("1. Biryani")
print("2. Chicken65")
print("3. Butter chicken")
print("4. Veg pulao")
print("5. PaneerTikka")
number = int(input("Enter your choice  "))
match number:
    case 1:
        print("Item: Biryani")
        print ("Price  : ₹220 ") 
        print ("Description: Delicious crispy hot chicken biryani")
    case 2:
        print("Item: Chicken65")
        print ("Price  : ₹250 ") 
        print ("Description:Crispy, fiery, and bursting with South Indian spice, our Chicken 65 is the ultimate crowd‑pleasing appetizer you can’t resist.")
    case 3:
        print("Item: Butter chicken")
        print ("Price  : ₹300 ") 
        print ("Description: Crispy and spicy deep-fried chicken pieces")
    case 4:
        print("Item: veg pula")
        print ("Price  : ₹150 ") 
        print ("Description: a simple rice dish made with vegetables, whole spices and herbs")
    case 5:
        print("Item:  PaneerTikka")
        print ("Price  : ₹280 ") 
        print ("Description: Pannerwith juicy")
    case _:
        print("no items listed")


#####    ATM MENU  ##################

print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

balance = 10000

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print(f"Current Balance: ₹{balance}")
    case 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposit successful. Remaining Balance: ₹{balance}")
    case 3:
        amount = int(input("Enter withdrawal amount: "))
        print(f"withdrawal succesful.reamining Balance: ₹{ balance-amount}")
    case 4:
        print("Thank you for using the ATM. Goodbye!")
    case _:
        print("Invalid choice. Please try again.")

##### Electricity Bill Calculator   ####

units = int(input("Enter units consumed: "))
if units >= 0 and units <= 100:
    amount = units * 2
    print(f"Electricity Bill is: ₹{amount}")

elif units >= 101 and units <= 200:
    amount = units * 4
    print(f"Electricity Bill is: ₹{amount}")

elif units >= 201 and units <= 300:
    amount = units * 6
    print(f"Electricity Bill is: ₹{amount}")

elif units > 300:
    amount = units * 8
    print(f"Electricity Bill is: ₹{amount}")

else:
    print("Invalid input. Units cannot be negative.")



#########    LEAP YEAR  #############
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

