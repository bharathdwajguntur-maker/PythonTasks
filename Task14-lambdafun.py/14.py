# 1. Calculate the total of three numbers
total = lambda a, b, c: a + b + c
print(total(5, 10, 15))

# 2. Find the difference between the larger and smaller number
difference = lambda a, b: a - b if a > b else b - a
print(difference(18, 25))

# 3. Find the double of a number
double = lambda n: n * 2
print(double(14))

# 4. Find the half of a number
half = lambda n: n / 2
print(half(20))

# 5. Check whether a number is divisible by both 2 and 3
check = lambda n: "Divisible" if n % 2 == 0 and n % 3 == 0 else "Not Divisible"
print(check(18))

# 6. Find the largest among three numbers
largest = lambda a, b, c: max(a, b, c)
print(largest(15, 28, 20))

# 7. Find the smallest among three numbers
smallest = lambda a, b, c: min(a, b, c)
print(smallest(15, 28, 20))

# 8. Find the remainder when one number is divided by another
remainder = lambda a, b: a % b
print(remainder(29, 6))

# 9. Calculate the total marks of three subjects
marks = lambda m1, m2, m3: m1 + m2 + m3
print(marks(75, 82, 68))

# 10. Calculate the percentage of marks
percentage = lambda total, maximum: (total / maximum) * 100
print(percentage(420, 500))

# 11. Check whether a person is a senior citizen
senior = lambda age: "Senior Citizen" if age >= 60 else "Not a Senior Citizen"
print(senior(65))

# 12. Check whether a number is a multiple of 10
multiple = lambda n: "Multiple of 10" if n % 10 == 0 else "Not a Multiple of 10"
print(multiple(70))

# 13. Calculate the cost of 5 items
cost = lambda price: price * 5
print(cost(40))

# 14. Convert hours into minutes
minutes = lambda hours: hours * 60
print(minutes(3))

# 15. Calculate the perimeter of a rectangle
perimeter = lambda length, breadth: 2 * (length + breadth)
print(perimeter(10, 6))

# 16. Check whether a character is a vowel
vowel = lambda ch: "Vowel" if ch in "aeiouAEIOU" else "Not a Vowel"
print(vowel("e"))

# 17. Find the age after 5 years
future_age = lambda age: age + 5
print(future_age(21))

# 18. Calculate the discount amount
discount = lambda price, percent: price * percent / 100
print(discount(2000, 15))

# 19. Calculate the final price after discount
final_price = lambda price, discount: price - discount
print(final_price(2000, 300))

# 20. Check whether a number lies between 10 and 50
check_range = lambda n: "Within Range" if 10 <= n <= 50 else "Outside Range"
print(check_range(35))