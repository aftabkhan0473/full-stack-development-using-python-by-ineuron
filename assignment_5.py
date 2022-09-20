# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
given_number = int(input("Enter a number which you like to remove the last digit : "))
final_number = int(given_number/10)
print(f"The final number by removing last digit is {final_number}")

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)

given_number2= int(input("Enter a number which you like to know last digit : "))
final_number2 = given_number2%10;
print(f"So Last digit of {given_number2} is {final_number2}")

# 3. Write a python script to swap data of two variables.

# first method 
first_one = int(input("Enter a number that would like to swap with second_one : "))
second_one = int(input("Enter a number that would like to swap with first_one : "))

# a_1 = first_one
# b_1= second_one
# second_one = a_1;
# first_one = b_1;
# print(f"first_one : {first_one}")
# print(f"second_one : {second_one}")

# second method 
first_one, second_one = second_one, first_one;  #osm hai bhai!
print(f"First number is {first_one}")
print(f"Second number is {second_one}")

# 4. Write a python script to find x power y, where values of x and y are given by user.

x_1 = int(input("Enter the first number : "))
y_1 = int(input("Enter the second number : "))
print(f"x_1 to the power y_1 is {x_1**y_1}")

# 5. Write a python script which takes a three digit numbber from the user and displays only its first digit.

three_digit_input = int(input("Enter a three digit number : "))
first_digit_of_three_digit = int(three_digit_input/100)
print(f"The first digit of {three_digit_input} is {first_digit_of_three_digit}")

# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.

three_digit_input = int(input("Enter a three digit number : "))
two_digit = three_digit_input%100;
middle_digit = int(two_digit/10)
print(f"The middle digit of that input three digit number is : {middle_digit}")
print(f"The last digit of that inputted three digit number is : {three_digit_input%10}")
print(f"The first digit : {int(three_digit_input/100)}")

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.

three_digit_number_2 = int(input("Enter the three digit number : "))
print(f"The last digit number is {three_digit_number_2%10}")

# 8. Write a python script to use IN operator to display the data present in list.

number_list = [1,2,3]
number = int(input("Enter an element you like to know that exist in list1 or not : "))
print(number in number_list)

# 9. Write a python script to use NOT IN operator to display the data not present in list.

string_list = ["Aftab", "Rahmat", "Raju", "Ali", "Shamsher"]
element_str = input("Enter the member which is not in your family with first name in capital letter : ")
print(element_str not in string_list)

#10. Write a python script to use IS operator to display if both variables are the same object or not?

variable1 = 15;
variable2 = 15;
print(variable1 is variable2)