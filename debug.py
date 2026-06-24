#1

age = 18

if age >=18:
    print ("Eligible to Vote")


#2
    
num = 10

if num == 10:
    print("Number is 10")


#3
    
marks = 75

if marks >= 50:
    print("Pass")


#4
    
num = -5

if num > 0:
    print("Positive")
    
else:
    print("Negative")


#5
    
temperature = 30

if temperature > 35:
    print("Hot")
elif temperature > 25:
    print("Warm")
else:
    print("Cool")


#6

username = "admin"

if username == "admin":
    print("Login Success")


#7
    
number = 10

if number > 5:
    print("Greater")
    
else:
    print("Smaller")


#8
    
value = 100

if value > 50:
    print("High")
    
else:
    print("Low")


#9
    
for i in range(5):
    print(i)


#10
    
for i in range (1,6):
    print(i)


#11
    
i = 1

while i <= 5:
    print(i)
    i+=1


#12

for i in range(5):
    print(i)


#13
    
numbers = [10, 20, 30]

for num in numbers:
    print(num)


#14
    
for i in range(5):
    print(i)
    i += 1


#15
    
i = 1
while i <= 5:
    print(i)
    i += 1


#16
    
for i in range(1, 11):
    if i == 5:
        print("Found")


#17
        
name = "Python"
print(name[4])


#18

text = "hello"
print(text.upper())


#19

message = "Welcome"
print(message.lower())


#20

word = "Python"
word='J'+word[1:]
print(word)


#21

name = "Praveen Kumar"
print(name.split())


#22

text = "Python"
for i in range(len(text)):
    print(text[i])


#23
    
language = "Python"
print(language + str(100))


#24

numbers = [10, 20, 30]
print(numbers[1])


#25

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


#26

fruits = ["Apple", "Orange"]
fruits.append("Banana")
print(fruits)


#27

numbers = [10, 20, 30]
numbers.remove(30)
print(numbers)


#28

numbers = [10, 20, 30]
print(len(numbers))


#29

names = ['A', 'B', 'C']
for i in range(len(names)):
    print(names[i])


#30
    
numbers = [10, 20, 30]
total = 0
for num in numbers:
    total = total + num

print(total)
