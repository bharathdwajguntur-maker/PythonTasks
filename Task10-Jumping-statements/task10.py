# BREAK
# 1. First even digit from left
n = 753914286
while n > 0:
    digit = n // 100000000
    if digit % 2 == 0:
        print("First even digit:", digit)
        break
    n = n % 100000000
    n = n * 10

# 2. First prime number between 50 and 100
for n in range(50, 101):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("First prime:", n)
        break

# 3. First number whose digit sum is 10
for n in range(1, 1000):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp = temp // 10
    if sum == 10:
        print("First number:", n)
        break

# 4. First number with exactly 3 divisors
for n in range(1, 101):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 3:
        print("First number:", n)
        break

# 5. Stop when 3 consecutive odd numbers occur
count = 0
for n in range(1, 51):
    if n % 2 != 0:
        count += 1
    else:
        count = 0
    if count == 3:
        print("Stopped at:", n)
        break

# 6. First palindrome between 10 and 500
for n in range(10, 501):
    temp = n
    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    if n == reverse:
        print("First palindrome:", n)
        break

# 7. First perfect number
for n in range(1, 1001):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print("First perfect number:", n)
        break

# 8. First 5 even numbers
count = 0
for n in range(1, 100):
    if n % 2 == 0:
        print(n)
        count += 1
    if count == 5:
        break

# 9. First 5 prime numbers
count = 0
for n in range(2, 100):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        print(n)
        count += 1
    if count == 5:
        break

# 10. First 3 numbers divisible by 7
count = 0
for n in range(1, 100):
    if n % 7 == 0:
        print(n)
        count += 1
    if count == 3:
        break

# CONTINUE

# 1. Print 1-30, skipping even numbers
for n in range(1, 31):
    if n % 2 == 0:
        continue
    print(n)

# 2. Print 1-40, skipping multiples of 4
for n in range(1, 41):
    if n % 4 == 0:
        continue
    print(n)

# 3. Print 1-30, skipping 10-20
for n in range(1, 31):
    if n >= 10 and n <= 20:
        continue
    print(n)

# 4. Print 1-50, skipping multiples of 3
for n in range(1, 51):
    if n % 3 == 0:
        continue
    print(n)

# 5. Extract 502304, skipping digit 0
n = 502304
while n > 0:
    digit = n % 10
    n = n // 10
    if digit == 0:
        continue
    print(digit)

# 6. Extract 5832461, printing only even digits
n = 5832461
while n > 0:
    digit = n % 10
    n = n // 10
    if digit % 2 != 0:
        continue
    print(digit)

# 7. Extract 1432578, skipping odd digits
n = 1432578
while n > 0:
    digit = n % 10
    n = n // 10
    if digit % 2 != 0:
        continue
    print(digit)

# 8. Print 1-200, skipping multiples of 3 or 5
for n in range(1, 201):
    if n % 3 == 0 or n % 5 == 0:
        continue
    print(n)

# 9. Print 1-500, skipping numbers with odd digit sum
for n in range(1, 501):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp = temp // 10
    if sum % 2 != 0:
        continue
    print(n)

# 10. Print 1-500, skipping numbers containing digit 0
for n in range(1, 501):
    temp = n
    found = False
    while temp > 0:
        digit = temp % 10
        if digit == 0:
            found = True
            break
        temp = temp // 10
    if found:
        continue
    print(n)

# break and continue
# 1. Print 1-50, skip multiples of 3, stop at 40
for n in range(1, 51):
    if n == 40:
        break
    if n % 3 == 0:
        continue
    print(n)

# 2. Print odd numbers, skip evens, stop at first multiple of 7
for n in range(1, 51):
    if n % 7 == 0:
        break
    if n % 2 == 0:
        continue
    print(n)

# 3. Extract 5830421, skip odd digits, stop at 0
n = 5830421
while n > 0:
    digit = n % 10
    n = n // 10
    if digit == 0:
        break
    if digit % 2 != 0:
        continue
    print(digit)

# 4. Extract 8325147, print digits until 5
n = 8325147
while n > 0:
    digit = n % 10
    n = n // 10
    if digit == 5:
        break
    print(digit)

# 5. Search from 51, skip non-multiples of 9, stop at first multiple
for n in range(51, 100):
    if n % 9 != 0:
        continue
    print("First multiple of 9:", n)
    break