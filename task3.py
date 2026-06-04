''' IF , IF ELIF ELSE , IF ELSE '''


#1. Accept two numbers and print quotient remainder
m = int(input("Enter m value : "))
n = int(input("Enter n value : "))
if m > n :
    quotient = m // n
    remainder = m % n
print("Quotient is : " , quotient)
print("Remainder is : ", remainder)


#2. Get marks and display grade

m1 = int(input("Enter mark 1 : "))
m2 = int(input("Enter mark 2 : "))
m3 = int(input("Enter mark 3 : "))
m4 = int(input("Enter mark 4 : "))
m5 = int(input("Enter mark 5 : "))

avg = ( m1 + m2 + m3 + m4 + m5 ) // 5
if avg >= 90:
    print("You have secured A grade ")
elif avg >= 70:
    print("You have secured B grade ")
elif avg >= 50 :
    print("You have secured C grade ")
elif avg >= 35:
    print("You have secured D grade ")
else:
    print("Sorry, You have Failed!")

print("----------------------")

#3. Positive or Negative number || even or odd || leap year or not

number = int(input("Enter a number :"))
if number % 2 == 0:
    print(number, "is a even number ")
else:
    print(number, "is a odd number")

if number > 0:
    print(number, "is a positive number")
elif number < 0:
    print(number, "is a negative number")
else:
    print(number, "is neither positive nor negative number")

if number % 4 == 0 and number > 0:
    print(number, "is a leap year ")
else:
    print(number, "is not a leap year ")


#4. Vowels and Consonants

char = input("Enter a character :")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' :
    print(char, "is a vowel ")
else:
    print(char, "is not a vowel ")
    

#5. Min and max of three numbers

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if( num1 <= num2 and num1 <= num3 ):
    print(num1, "is the minimum number")
elif ( num2 <= num1 and num2 <= num3 ):
    print(num2, "is the minimum number")
else:
    print(num3, "is the minimum number")


if( num1 >= num2 and num1 >= num3 ):
    print(num1, "is the maximum number")
elif ( num2 >= num1 and num2 >= num3 ):
    print(num2, "is the maximum number")
else:
    print(num3, "is the maximum number")


#6.Season of the month

month = input("Enter a month : ")
if( month == "december" or month == "january" or month == "february" ):
    print(month, "has winter season")
elif( month == "march" or month == "april" or month == "may" ):
    print(month, "has summer season")
elif( month == "june" or month == "july" or month == "august" or month == "september"):
    print(month, "has monsoon season")
elif( month == "october" or month == "november" ):
    print(month, "has post monsoon season")
else:
    print("Invalid input")

#7. Number of days in a month

month = input("Enter a month : ")
year = int(input("Enter the year: "))
if( month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december" ):
    print(month, "has 31 days")
elif( month == "april" or month == "june" or month == "september" or month == "november"):
    print(month, "has 30 days")
elif( month == "february"):
    if(year % 4 == 0):
        print(month, "has 29 days")
    else:
        print(month, "has 28 days")
else:
    print("Invalid input")


#8. multiples of 5

number = int(input("Enter a number :"))
if number % 5 == 0:
    print("Hello")
else:
    print("Bye")


#9. Celsius for boiling water

cel = int(input("Enter the degree in celsius :"))
if cel == 100:
    print("Water is getting boiled")
else:
    print("Water is not getting boiled")


#10. Charge for library

days = int(input("Enter the days : "))
charge = 0
if days >= 1 and days <= 5:
    charge = days * 2
elif days >= 6 and days <= 10:
    charge = days * 3
elif days >= 11 and days <= 15:
    charge = days * 4
elif days > 15 :
    charge = days * 5
else:
    print("Enter valid days")

print("Charges for ",days," days is ",charge)


#11. Police work eligiblity

age = int(input("Enter the age: "))
nationality = input("Enter the nationality: ")
tamil_proficiency = bool(input("Proficient in tamil (True / False ) ? :"))

if( (age >=18 and age <= 32) and nationality == "Indian" and tamil_proficiency == True ):
    print("Eligible for Police Work")
else:
    print("Not Eligible for Police Work")


#12. Employee bonus calculation

salary = int(input("Enter annual salary :"))
bonus_percent = int(input("Enter bonus percentage:"))

bonus = salary * (bonus_percent/100)

print("Bonus : ", bonus)


#13.Calculate Current Fare

units = int(input("Enter the units used : "))
if units > 0 and units <= 100:
    print("Charge = 0 ")
elif units > 100 and units <= 400:
    print("Charge =  ", units * 5)
elif units > 401 and units <= 500:
    print("Charge = ", units * 7)
elif units > 500 and units <= 600:
    print("Charge = ", units * 9)
elif units > 600 and units <= 800:
    print("Charge = ", units * 10)
elif units > 800 and units <= 1000:
    print("Charge = ", units * 11)
elif units > 1000:
    print("Charge = ", units * 12)
else:
    print("Enter valid unit")


#14. Password Validation

email = input("Enter your email id : ")
if email == "sugan2002@gmail.com":
    password = int(input("Enter your password : "))
    if(password == 12345) :
        print("Correct Password- Login successful")
    else:
        print("Incorrect Password")
else:
    print("Enter valid e-mail")
    

    
