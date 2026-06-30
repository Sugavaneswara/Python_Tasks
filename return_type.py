#1. is_even()

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
result = is_even(n)
print(result)

#2. Largest()

def largest(a,b,c):
def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
result = largest(a,b,c)
print(result)

#3. Factorial()

def factorial(n):
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
result = factorial(n)
print(result)

#4. reverse()

def reverse(n):
    rev = 0
    while n > 0 :
        last = n % 10
        rev = rev * 10 + last
        n //= 10
    return rev

n = int(input("Enter a number: "))
result = reverse(n)
print(result)

#5. sum_of_digits()

def sum_of_digits(n):
    sum = 0
    while n > 0:
        last = n % 10
        sum += last
        n //= 10

    return sum

n = int(input("Enter a number: "))
result = sum_of_digits(n)
print(result)


#6. count_even_digits()

def count_even_digits(n):
    count = 0
    while n > 0:
        last = n % 10
        if last % 2 == 0:
            count += 1
        n //= 10
    return count

n = int(input("Enter a number: "))
result = count_even_digits(n)
print(result)

#7. Palindrome()

def is_palindrome(n):
    temp = n
    rev = 0

    while temp > 0:
        last = temp % 10
        rev = rev * 10 + last
        temp //= 10

    if rev == n:
        return "Palindrome"
    else:
        return "Not Palindrome"

n = int(input("Enter a number: "))
result = is_palindrome(n)
print(result)

#8. second_largest()

def second_largest(l):
   max = 0
   second_max = 0
   for i in l:
       if i > max and i > second_max:
           second_max = max
           max = i
       elif i < max and i > second_max:
           second_max = i

   return second_max

l = [5,1,12,8,5,7]
result = second_largest(l)
print(result)

#9. remove_duplicates()

def remove_duplicates(l):
    temp = []
    for i in l:
        if i not in temp:
            temp.append(i)
    return temp

l = [1,2,3,4,2,3,5,6,7,6]
result = remove_duplicates(l)
print(result)


#10. count_vowels()

def count_vowels(text):
    count = 0
    for i in text:
        if i in 'aeiouAEIOU':
            count += 1
    return count

text = input("Enter a string: ")
result = count_vowels(text)
print(result)


#11. common_elements(l1,l2)

def common_elements(l1,l2):
    common = []

    for i in l1:
        if i in l2:
            common.append(i)
    return common

l1=[1,2,3,4,5,6,7,8]
l2=[1,2,3,9,10,11,4,12]
result = common_elements(l1,l2)
print(result)