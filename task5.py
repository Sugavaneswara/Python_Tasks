#1. Square Pattern

for i in range(5):
    for j in range(5):
        print("*",end  = " ")
    print()

#2. Hollow Square

for i in range(5):
    for j in range(5):
        if(i == 0 or i == 4 or j == 0 or j == 4):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()


#3. Plus  Pattern

for i in range(5):
    for j in range(5):
        if(i == 2 or j == 2):
            print("*",end = " ")
        else:
            print(" ", end = " ")
    print()


#4. Cross Pattern

for i in range(5):
    for j in range(5):
        if( i == j or i + j == 4):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()


#5. Cross APPLE Pattern

for i in range(5):
    for j in range(5):
        if i == 0 and j == 0:
            print(chr(65), end = " ")
        elif i == 1 and j == 1:
            print(chr(80), end = " ")
        elif i == 2 and j == 2:
            print(chr(80), end = " ")
        elif i == 3 and j == 3:
            print(chr(76), end = " ")
        elif i == 4 and j == 4:
            print(chr(69), end = " ")
        elif i == 0 and j == 4:
            print(chr(65), end = " ")
        elif i == 1 and j == 3:
            print(chr(80), end = " ")
        elif i == 3 and j == 1:
            print(chr(76), end = " ")
        elif i == 4 and j == 0:
            print(chr(69), end = " ")
        else:
            print(" ", end = " ")
    print()


#6. Cross Plus Pattern

for i in range(5):
    for j in range(5):
        if i == 0 and j == 2:
            print(chr(97), end = " ")
        elif i == 1 and j == 2:
            print(chr(112), end = " ")
        elif i == 2 and j == 2:
            print(chr(112), end = " ")
        elif i == 3 and j == 2:
            print(chr(108), end = " ")
        elif i == 4 and j == 2:
            print(chr(101), end = " ")

        elif i == 2 and j == 0:
            print(chr(97), end = " ")
        elif i == 2 and j == 1:
            print(chr(112), end = " ")
        elif i == 2 and j == 3:
            print(chr(108), end = " ")
        elif i == 2 and j == 4:
            print(chr(101), end = " ")
        else:
            print(" ", end = " ")
        
    print()


#7. Hollow square with character

char = 90
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end = " ")
        else:
            print(chr(char), end = " ")
            char -= 1
    print()


#8. Full Pyramind

for i in range(5):
    for j in range(i,5):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()
        

#9. Inverted pyramid

for i in range(5):
    for j in range(i + 1):
        print(" ", end = " ")
    for j in range(i,5):
        print("*", end = " ")
    for j in range(i,4):
        print("*", end = " ")
    print()


#10. Triangle Pattern

for i in range(5):
    for j in range(i + 1):
        print(" ", end = " ")
    for j in range(i,5):
        if i == 0 or i == j:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    for j in range(i,4):
        if i == 0 or ( j == 3 ) :
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()


#11. Factorial

num = int(input("Enter the number for factorial : "))
fact = 1
for i in range(1,num+1):
    fact *= i

print("Factorial of ",num, " is ",fact)


#12. Increment while loop

num = 1
while num <= 20 :
    print(num)
    num += 1


#13. Decrement While loop

num = 20
while num >= 1:
    print(num)
    num -= 1


#14. Infinite while loop

num = 1
while num > 0:
    print(num)
    num += 1
