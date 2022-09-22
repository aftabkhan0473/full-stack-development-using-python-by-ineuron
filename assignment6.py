# 1. Write a python script to check whether a given number is positive or non-positive.

input_number = int(input("Enter a number : "))
if(input_number>0):
    print(f"{input_number} is positive!")
else:
    print(f"{input_number} is non-positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not

input2 = int(input("Enter a number : "))
if(input2%5==0):
    print(f"{input2} is divisible by 5")
else:
    print(f"{input2} is not divisible by 5")

# 3. Write a python script to check whether a given number is even or odd.

input3 = int(input("Enter a number : "))
if(input3%2==0):
    print(f"{input3} is even")
else:
    print(f"{input3} is odd")

# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

input_1 = int(input("Enter first number : "))
input_2 = int(input("Enter second number : "))
if(input_1>input_2):
    print(f"{input_1} is greater than {input_2})")
elif(input_1==input_2):
    print(f"Both are same!")
else:
    print(f"{input_1} is less than {input_2}")

# 5. Write a python script to print two given words in dictionary order.



#6. Write a python script to check whether a given number is three digit numer or not.

no_1 = int(input("Enter a number : "))
str_no = str(no_1)
if(len(str_no)==3):
    print(f"Yes {no_1} is three digit no.")
else:
    print("No, it's not a three digit number")