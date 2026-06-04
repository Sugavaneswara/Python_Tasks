''' For Loop, Patterns and Membership operators '''

#1. Check List element (20)

numbers = [10,20,30,40,50]
if 20 in numbers:
    print("The number 20 is present")
else:
    print("The number 20 is not present")


#2. Check List element (100)

numbers = [10,20,30,40,50]
if 100 in numbers:
    print("The number 100 is present")
else:
    print("The number 100 is not present")


#3. Check String element (P)

name = "Python"
if 'P' in name:
    print("The letter P is present in the string Python")
else:
    print("The letter P is not present in the string Python")


#4. Check String element (Z)

name = "Python"
if 'z' not in name:
    print("The letter z is not present in the string Python")
else:
    print("The letter z is present in the string Python")


#5. List of fruits (check Apple)

fruits = ["Mango","Pineapple","Strawberry","Apple","Banana"]
if "Apple" in fruits:
    print("Apple is present in the list of fruits")
else:
    print("Apple is not present in the list of fruits")


#6. Print numbers 1 to 10

for i in range(1,11):
    print(i)


#7. Print numbers 5 to 15

for i in range(5,16):
    print(i)


#8. Print even numbers 2 to 20

for i in range(2,21,2):
    print(i)


#9. Print odd number 1 to 20

for i in range(1,20,2):
    print(i)


#10. Print multiples of 10 till 100

for i in range(10,101,10):
    print(i)


#11. Print multiples of 5

for i in range(5,51,5):
    print(i)


#12. Multiple table of user input

n = int(input("Enter the table's number : "))
for i in range(n, (n*10) + 1,n):
    print(i)


#13.Sum from 1 to 10

sum = 0
for i in range(1,11):
    sum += i
print(sum)


#14. Sum from 1 to 20

sum = 0
for i in range(1,21):
    sum += i
print(sum)


#15. Squares from 1 to 10

for i in range(1,11):
    print(i ** 2)


#16. Print from 10 to 1

for i in range(10,0,-1):
    print(i)


#17. Print from 20 to 1

for i in range(20,0,-1):
    print(i)


#18. Even from 20 to 2

for i in range(20,1,-2):
    print(i)


#19. Odd from 19 to 1

for i in range(19,0,-2):
    print(i)


#20. Print 10 to 0

for i in range(10,-1,-1):
    print(i)


#21. Print 50 to 0 and gap 5

for i in range(50,-1,-5):
    print(i)


#22. User input to 1

n= int(input("Enter the reverse starting number : "))
for i in range(n,0,-1):
    print(i)


#23. Multiple table of 5 in reverse

for i in range(50,-1,-5):
    print(i)


#24. Each character in new line

for i in "Python":
    print(i)


#25. Each character from input

name = input("Enter your name : ")
for i in name:
    print(i)


#26. Count characters in string

name = input("Enter your name : ")
count = 0
for i in name:
    count += 1
print("Number of characters : ",count)


#27. Count vowels in string

name = input("Enter your name : ")
count = 0
for i in name:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'): 
        count += 1
print("Number of vowels : ",count)


#28. 5x5 # pattern

for i in range(5):
    for j in range(5):
        print("#",end = " ")
    print()
    

#29. Half Pyramid pattern

for i in range(5):
    for j in range(i + 1):
        print(j,end =" ")
    print()


#30. Inverted number pattern

for i in range(5):
    for j in range(i,5):
        print(j,end  = " ")
    print()
