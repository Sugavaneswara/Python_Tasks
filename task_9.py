#1. Length of the string

String = input("Enter a String : ")
length = 0

for i in String:
    length += 1
    
print("Length of the String : ",length)


#2. Check isalpha()

String = input("Enter a String : ")

print(String.isalpha())


#3. Check isdigit()

String = input("Enter a String : ")

print(String.isdigit())


#4. Consonants count

String = input("Enter a String : ")
consonants = 0

for i in String:
    
    if i.isalpha() and i not in "aeiouAEIOU":
        consonants += 1
        
print("Number of Consonants : ",consonants)


#5. Non-repetive character

String = input("Enter a String : ")

for i in String:
    if String.count(i) == 1:
        print(i)
        break

#6. swapcase()
    
String = input("Enter a String : ")

print(String.swapcase())


#7. Remove Spaces

String = input("Enter a String : ")
temp = ""

for i in String:
    if i != " ":
        temp += i
        
print(temp)

#8. Check String starts with vowel

String = input("Enter a String : ")

for i in String:
    if String[0] in "aeiouAEIOU":
        print("String starts with a vowel")
    else:
        print("String does not starts with a vowel")


#9. Number of occurence of a character

string = input("Enter a String : ")
char = input("Enter the Character to be found : ")

char_count = 0

for i in string:
    if i == char:
        char_count += 1

if char_count == 0:
    print("Character not found")
    
else:
    print(char_count)


#10. Replace vowels with *

String = input("Enter a String : ")
temp = ""

for i in String:
    if i in "aeiouAEIOU":
        temp += "*"
    else:
        temp += i
        
print(result)


#11. Even index elements

String = input("Enter a String : ")

for i in range(0, len(String), 2):
    
    print(String[i], end=" ")
    

#12. Odd index elements
    
String = input("Enter a string : ")

for i in range(1, len(String), 2):
    print(String[i], end=" ")


#13. String elements to list
    
String = input("Enter a string:")
list_element = []

for i in String:
    list_element.append(i)
    
print(list_element)


#14. Special character count

String = input("Enter a String : ")
count = 0

for i in String:
    
    if not i.isalnum() and i != " ":
        count +=1

print(count)


#15. isalnum()

String = input("Enter a String : ")

if String.isalnum():
    print("TRUE")
else:
    print("FALSE")


#16. Remove leading and trailing space without split()

String = input("Enter a string : ")


for i in String:
    if i != " ":
        start  = String.index(i)
        break

for i in String[::-1]:
    if i != " ":
        end = String.rindex(i)
        break

print(String[start:end+1])


#17. ASCII value

String = input("Enter a String : ")
for i in String:
    print(ord(i))


#18. Split spaces without split()

String = input("Enter a string : ")
word = ""

for i in String:
    if i != " ":
        word += i
    else:
        print(word)
        word = ""

print(word)


#19. Longest word in a string

String = input("Enter a string : ")

temp = String.split()

longest_word = temp[0]

for i in temp:
    if len(i) > len(longest_word):
        longest_word = i
        
print(longest_word)


#20. Check Identifier

String = input("Enter a String : ")

check = String.isidentifier()
print(check)
