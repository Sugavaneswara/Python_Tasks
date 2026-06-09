#1. Factorial

num = int(input("Enter a number for which factorial needs to be found : "))
fact = 1

for i in range(1,num+1):
    fact *= i
print("Factoial : ",fact)


#2. First 10 natural number using for and while loop

for i in range(1,11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
    

#3. Sum of first 10 natural numbers

i = 1
sumofnumbers = 0
while i <= 10:
    sumofnumbers += i
    i += 1
print("Sum = ",sumofnumbers)    


#4. Multiplication table of input

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, " x ", i , " = ", num * i)


#5. Fibonacci

num = int(input("Enter a number : "))
n1 = 0
n2 = 1

for i in range(1,num+1):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

#6. Palindrome

num = int(input("Enter a number : "))
reverse = 0
temp = num

while temp > 0:
    last = temp % 10
    reverse = reverse * 10 + last
    temp = temp // 10

if reverse == num:
    print(f"{num} is a palindrome ")
else:
    print(f"{num} is not a palindrome ")
   

#7. Armstrong number

num = int(input("Enter a number : "))
temp = num
arm = 0
n = 0

while temp > 0:
    last = temp % 10
    n += 1
    temp = temp // 10

temp = num
    
while temp > 0:
    last = temp % 10
    arm += last ** n
    temp = temp // 10

if arm == num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")


#8. HCF of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF = ", hcf)


#9. Multiples of 3 and 5 with msg

for i in range(1,51):
    if i % 3 == 0 and i %  5 == 0:
        print(i, " hihello")
    elif i % 3 == 0:
        print(i, " hi")
    elif i % 5 == 0:
        print(i, " hello")


#10. Prime number

num = int(input("Enter a number : "))
if num <= 1:
    print("Not a prime number")

else:
    for i in range (2, num):
        if num % i == 0:
            print("Not a prime number")
            break;
    else:
        print("Prime Number")


#11. Prime from 1 to 100

for num in range(2,101):
    for i in range (2, num):
        if num % i == 0:
            break;
    else:
        print(num, end = " ")


#12. Positive Divisors

num = int(input("Enter a number : "))

for i in range(1,num+1):
    if num % i == 0:
        print(i)


#13. Sum of first n odd and even numbers

n = int(input("Enter a value: "))
odd_sum = 0
even_sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Odd number's sum : ", odd_sum)
print("Even number's sum : ", even_sum)


#14. Perfect Square

num = int(input("Enter a number: "))

root = int(num ** 0.5)

if root * root == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")



















