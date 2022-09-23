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