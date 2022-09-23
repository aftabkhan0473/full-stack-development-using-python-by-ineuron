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

# 7. Write a python script to check whether a given number is positive, negative or zero.

no_2 = int(input("Enter a number : "))
if(no_2>0):
    print(f"{no_2} is positive")
elif(no_2==0):
    print(f"{no_2} is zero")
else:
    print(f"{no_2} is negative")

# 8. Write a python script to check whether a  given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots


#9. Write a python script to check whether a given year is a leap year or not.

year = int(input("Enter year : "))

# condition : divisible by 4 but not 100 if divisible by 100 then also divisible by 400

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year")

# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.


# 11. Write a python script to take the month value in numeric format and display the number of days in it.

month_number = int(input("Enter the month in numeric form : "))

if(month_number==1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number ==8 or month_number == 10 or month_number == 12):
    print(f"The total number of days in this month is 31")
elif(month_number==2):
    year = int(input("Enter year : "))
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                year_leap = "leap";
            else:
                year_leap = "not_leap";
        else:
            year_leap = "leap";
    else:
        year_leap = "not_leap";
    if(year_leap=="leap"):
        print(f"The total days in this month is 29")
    else:
        print(f"The total days in this month is 28")
else:
    print(f"The total days of this month is 30")