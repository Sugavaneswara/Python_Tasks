#1. String is palindrome or not

String = input("Enter a string : ")

temp = ""

for i in String:
    temp = i + temp

if temp == String:
    print("True")
else:
    print("False")


#2. Count number of vowels

String = input("Enter a string : ")

vowel_count = 0

for i in String:
    if i in "aeiouAEIOU":
        vowel_count += 1

print("No of Vowels : ",vowel_count)
    

#3. Reverse a string

String = input("Enter a string : ")

Reverse = ""

for i in String:
    Reverse = i + Reverse

print(Reverse)


#4. Count upper and lower case

String = input("Enter a string : ")
lower_count = 0
upper_count = 0

for i in String:
    if i in "qwertyuiopasdfghjklzxcvbnm":
        lower_count += 1
    elif i in "QWERTYUIOPLKJHGFDSAZXCVBNM":
        upper_count += 1

print("Number of uppercase letters : ", upper_count)
print("Number of lowercase letters : ", lower_count)


#5. Remove all dupliates

String = input("Enter a string : ")

temp = ""

for i in String:
    if i not in temp:
        temp = temp + i

print(temp)


#6. Frequent character

String = input("Enter a string : ")

temp = ""
freq = ""

for i in String:
    if i not in temp:
        temp = temp + i
    else:
        freq = freq + i

print(freq)


#7. Anagrams

String_1 = input("Enter 1st string : ")
String_2 = input("Enter 2nd string : ")
count = 0

for i in String_1:
    if i in String_2:
        count += 1

if count == len(String_1) :
    print("True")
    
else:
    print("False")


#8. Remove all non character

String = input("Enter a string : ")
temp = ""

for i in String:
    if i in "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM":
        temp = temp + i

print(temp)


#9. Count number of words

String = input("Enter a string : ")
l = String.split(" ")
count = 0

for i in l:
    count += 1

print(count)  
    

#10. Sum of digits in String

String = input("Enter a string : ")
total = 0

for i in String:
    if i in "0123456789":
        total += int(i)

print(total)


#11. Replace " " withString = input("Enter a string : ")

String = input("Enter a string : ")
l = String.split(" ")
temp = "-".join(l)

print(temp)


#12. Capitalize first character of all words

String = input("Enter a string : ")

temp = String.title()

print(temp)


#13. Sum of digits

String = input("Enter a string : ")
temp = ""

for i in String:
    if i in "0123456789":
        temp = temp + i

print(temp)


#14. Every second character

String = input("Enter a string : ")
print(String[1::2])


#15. Starts and end with]

String = input("Enter a string : ")

print(String.startswith("i"))
print(String.endswith("an"))
