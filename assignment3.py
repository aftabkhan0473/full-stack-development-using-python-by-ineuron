# 1. Write a python script to convert a number into str type.

from unicodedata import decimal


int_user = int(input("Enter a number : "))
convert_int = str(int_user)
print(convert_int)
print(type(convert_int))

# 2. Write a python script to print Unicode of the character "m".

unicode_of_character = "m";
# unicode = "md" # error just because ord function to find unicode can contain only one character! that is string of only one length
print(ord(unicode_of_character)) # ord function to find unicode of a character
# print(ord(unicode)) # encounter erro! just because unicode consist of string of length more than one!

# 3. Write a python script to print character representation of a given unicode 100.

character_unicode = 100;
print(chr(character_unicode)) # chr function to find the character of that unicode !

a1 = 1540;
print(chr(a1))
# a2,a3,a4,a5,a6 = 1,120,1,10,155;
# print(chr(a2),chr(a3),chr(a4),chr(a5),sep="\n", end="")

print(chr(1))
print(chr(120))
print(chr(100))
print(chr(1540))
print(chr(3))
print(chr(4))
print(chr(5))
print(chr(6))
print(chr(7))
print(chr(8))
print(chr(9))
print(chr(2))

# Note : ord to find the unicode of single string and chr function is to find character of that unicode!

# 4. Write a python script to print any number and its binary equivalent

user_number = int(input("Enter any number which binary you like to know : "))
print(f"the binary of that input number is {bin(user_number)}")

# 5. Write a python script to print any numberr and its octal equivalent.

user_number2 = int(input("Enter any number you like to know its octal value : "))
print(f"The octal value of input number is {oct(user_number2)}")

# 6. Write a python script to print any number and its hexadecimal equivalent.

user_number3 = int(input("Enter a number you like to know its hexadecimal value : "))
print(f"The hexadecimal value of that input number is {hex(user_number3)}")

# 7. Wrie a python script to store binary number 1100101 in a variable and print it in decimal format.

binary_input = input("Enter a binary number : ");
list_binary = list(binary_input)
list_binary.reverse() #can't store this in a variable!
decimal = 0;

for i in range(len(binary_input)):
    decimal = decimal + int(list_binary[i])*2**i;

print(decimal)

