#1. Series
def series1():
    for i in range(2,17,2):
        print(i)

series1()

#2. Series

def series2():
    for i in range(50,-1,-10):
        print(i)

series2()

#3. Square

def square(a):
    print(a**2)

a = int(input("Enter a number: "))
square(a)

#4. Cube

def cube(a):
    print(a**3)

a = int(input("Enter a number: "))
cube(a)

#5. Split Digits

def split_digits(n):
    while n>0:
        last = n % 10
        n = n // 10
        print(last,end = " ")

n = int(input("Enter a number: "))
split_digits(n)

#6. Armstrong Number

def armstrong(n):
    temp = n
    count = 0
    while temp > 0:
        temp = temp // 10
        count += 1

    sum = 0
    temp2 = n
    while temp2 > 0:
        last = temp2 % 10
        sum += last ** count
        temp2 = temp2 // 10

    if sum == n:
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")

n = int(input("Enter a number: "))
armstrong(n)

#7. Spy Number

def spy_numbers(n):
    temp = n
    sum = 0
    while n > 0:
        last = n % 10
        sum += last
        n = n // 10

    prod = 1
    while temp > 0:
        last = temp % 10
        prod *= last
        temp = temp // 10

    if sum == prod:
        print("It is an spy number")
    else:
        print("It is not an spy number")

n = int(input("Enter a number: "))
spy_numbers(n)

#8. Reverse Square

def rev_square(n):
    while n > 0:
        last = n % 10
        print(last ** 2,end = " ")
        n = n // 10

n = int(input("Enter a number: "))
rev_square(n)

#9. Count Digits

def count_digits(n):
    count = 0
    while n > 0:
        last = n % 10
        count += 1
        n = n // 10
    print(count)

n = int(input("Enter a number: "))
count_digits(n)

#10. Sum of Divisors

def sum_of_divisors(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
           sum += i
    print(sum)

n = int(input("Enter a number: "))
sum_of_divisors(n)

#11. Price and Discount

def input_price():
    price = int(input("Enter the price : "))
    calculate_charge(price)

def calculate_charge(price):
    if price >= 50000:
        price = price - (price * (10/100))
        print(price)
    elif price >= 30000 and price <= 49999:
        price = price - (price * (5/100))
        print(price)
    else:
        price = price - (price * (2/100))
        print(price)

input_price()

#12. Add Values

def add_values(a,b):
    sum = a + b
    print(sum)

a = int(input("Enter a number: "))
b = float(input("Enter a number: "))

add_values(a,b)

#13. Check Capital

def is_capital(ch):
    if ch.isupper():
        print("Capital Character")
    else:
        print("Not a Capital Character")

ch = input("Enter a character: ")
is_capital(ch)

#14. Check Vowel

def is_vowel(ch):
    if ch in 'aeiou':
        print("Character is vowel")
    else:
        print("Character is not vowel")

ch = input("Enter a character: ")
is_vowel(ch)

#15. Lower

def to_lower_case(ch):
    if ch.islower():
        print(ch)
    else:
        print(ch.lower())

ch = input("Enter a character: ")
to_lower_case(ch)
