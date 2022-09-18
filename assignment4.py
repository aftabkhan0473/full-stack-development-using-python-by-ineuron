# 1. Write a python script to take your name as input from the user and then print it.
from socket import if_nametoindex
from time import time


input_name = input("Enter your name : ")
print(f"Your name is {input_name}")

# 2. Write a python script to take input from the user. Input must be a number.

input_number = input("Enter a number : ")
print(type(input_number)) #input can't be a int input is as always str@

# 4. Write a python script which takes the radius from the user and display area of a circle.
input_radius = int(input("Enter the radius of circle : "))
print(f"The area of that circle having radius {input_radius} is {(22/7)*(input_radius**2)}")

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.

first_number1 = int(input("Enter the first number : "))
second_number1 = int(input("Enter the second number : "))
print(f"The sum of {first_number1} and {second_number1} is {first_number1+second_number1}")

# 5. Write a python script to calculate the square of a number. Numbered is entered by the user.

num1 = int(input("Enter the number which you like to know square : "))
print(f"The square of {num1} is {num1**2}")

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.

height_triangle = int(input("Enter the height of triangle : "))
base_triangle = int(input("Enter the base side of triangle : "))
print(f"The are of triangle having height {height_triangle} and base {base_triangle} is {1/2*height_triangle*base_triangle}")

# 7. Write a python script to calculate average of three numbers, entere by the user

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
num_3 = int(input("Enter third number : "))
print(f"The average of {num_1}, {num_2} and {num_3} is {(num_1+num_2+num_3)/3}")

# 8. Write a python script to calculate simple interest.

principal_value = int(input("Enter the principal value : "))
rate_value = int(input("Enter the rate for that principal : "))
time_value = int(input("Enter the total time : "))

total_simple_rate = (principal_value*rate_value*time_value)/100
print(f"The value of simple rate for {time_value} is {total_simple_rate}")

# 9. Write a python script to calculate the volume of a cuboid.
side1 = int(input("Enter the length of first side of cuboid : "))
side2 = int(input("Enter the side of second side of cuboid : "))
side3 = int(input("Enter the length of third side of cuboid : "))
print(f"The value of volume of that cuboid having sides are {side1},{side2} and {side3} is {side1*side2*side3}")

# 10. Write a python script to calculate aera of a rectangle.
side1_of_rectangle = int(input("Enter the first side of that rectangle : "))
side2_of_rectangle = int(input("Enter the second side of that rectangle : "))
print(f"The area of that rectangle is {side1_of_rectangle*side2_of_rectangle}")