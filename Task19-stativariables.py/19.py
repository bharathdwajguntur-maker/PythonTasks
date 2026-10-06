# class Bank:
#     bank_name="union"
#     def __init__(self,name,branch,num):
#         self.name=name
#         self.branch=branch
#         self.num=num
#     def display(self):
#         print(Bank.bank_name,"holder name is",self.name)
#         print(Bank.bank_name," branch area is",self.branch)
#         print(Bank.bank_name," holder mobile number is",self.num)
# b=Bank("bharath","guntur","123456789")``
# b.display()

# class Product:
#     platform = "myntra.com"
#     def __init__(self, product_id, product_name, price):
#         self.product_id = product_id
#         self.product_name = product_name
#         self.price = price

#     def display(self):
#         print(Product.platform, "is the best platform to buy")
#         print(self.product_id, "is the best one")
#         print(f"Product Name: {self.product_name}, Price: ₹{self.price}\n")

# prod1 = Product("P101", "Casual Shirt", 1299)
# prod2 = Product("P102", "Running Shoes", 2499)

# prod1.display()
# prod2.display()
 
# class Vehicle:
#     company_name = "Apex Logistics"
#      Type= "Galileo-v4"

#     def __init__(self, vin, model, driver_name, fuel_level):
#         self.vin = vin
#         self.model = model
#         self.driver_name = driver_name
#         self.fuel_level = fuel_level

#     # Method to display all variables
#     def display_status(self):
#         print(f"--- Fleet: {Vehicle.company_name} (GPS: {Vehicle.Type}) ---")
#         print(f"VIN: {self.vin}")
#         print(f"Model: {self.model}")
#         print(f"Driver: {self.driver_name}")
#         print(f"Fuel Level: {self.fuel_level}%\n")

# truck1 = Vehicle("1FA6P8CF0H", "Freightliner Cascadia", "Carlos Ruiz", 85)
# truck2 = Vehicle("1FA6P8CF1M", "Volvo VNL 860", "Sarah Jenkins", 42)

# truck1.display_status()
# truck2.display_status()
