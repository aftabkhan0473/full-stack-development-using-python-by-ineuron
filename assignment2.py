# 1. Write a python script to add comments and print "Learning Python" on the screen.
print("Learning python")

# 2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.
a = """
To,
    The principal,
    Holy Mission Public School
    Majhaulia Muzaffarpur Bihar 843104

Dear Sir,
        Most humbly and respectfully i beg to say that I am ill with fever so i can't attend the class so dear sir i would like to take a leave for today!
                                                        Therefore, i kindly request you to give me
        today's leave. I am so thankful to you for this!


                                                            Your faithfully,
                                                            MD AFTAB ALI    
                                                            Father's name : MD ALI RAZA
                                                            Class : part 3
                                                            Roll no : 
                                                            College : B.D COLLEGE, PATNA
                                                        
"""
# NOTE:- There are nothing in python for multi-line comment if you like to do multi-line comment then yes you have to comment one by one and you can select all and tap ctrl+/

print(a)
# so dekha as, it is print karne ke liye triple quotes """ """ hai 🥰

# 2.Ans
# var1 = 10;
# var2 = "a";
# var3 = 1.0;
# var4 = True;

var1,var2,var3,var4 = 10,"a", 1.0, True;
print(var1,var2,var3,var4, sep="\n")

# 3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. 

var_1,var_2,var_3,var_4 = 1,1.5,True,3+4j;
print(var_1,var_2,var_3,var_4, sep="\n")

# 4. Write a python script to print the id of two variables containing the same integer values.
var__1 = 5;
var__2 = 5;
print(id(var__1))
print(id(var__2)) # so notice here, id of two variables containing same element is same.

# 5. Create four variables in a python script and assign values of different data types to them. Write a python script to print value, its type and id of each variable.
var___1 = 1.0;
var___2 = 2+4j;
var___3 = 9;
var___4 = True;
var___5 = True; # it's id is fixed i.e 140713833166952
print(type(var___1))
print(type(var___2))
print(type(var___3))
print(type(var___4))
print(type(var___5))
print(id(var___1))
print(id(var___2))
print(id(var___3))
print(id(var___4))
print(id(var___5))

# 6. Write a python script to pribn all the keywords

import keyword

print(keyword.kwlist)

# 7. On python shell use help() function and display the list of keywords.

# help()
# keywords

# 8. Create two python files A0.py and A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py

# see A0 file and A1 file 

# 9.Name the keywords, used as data in the python script. 


# 10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 16-9-2022) and 12:00PM