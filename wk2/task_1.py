# Exercise 1: Age Calculator

"""
Create a program that:
1. Asks the user to input their birth date in mm/dd/yyyy format
2. Validates the input format and ensures it’s a valid date
3. Calculates and displays their current age in years
4. Converts and displays the birthdate in European format (dd/mm/yyyy)
5. Handles all possible errors gracefully with appropriate messages

"""
# in order to deal with dates and calculation based on real time , we use built in module here called datetime
from datetime import datetime

while True:     # in order to ask again if entered date is wrong we use while to ask repeatedly
    DOB=input("enter the dob in MM/DD/YYYY format\n").strip()

    try:
        AGE=datetime.strptime(DOB,"%m/%d/%Y") # in order to convert string form of date into python understandable formate we use strptime to take in m/d/y forrmate

        TODAY=datetime.today() # today() gives u todays exact date with month and year and time also in hr/min/sec

        # now we have to validate the date entered by user 
        if AGE>TODAY: # Checking user entered future date
            print("You have entered wrong date. Please check")
            continue
        else: # if entered age is right 
            Current_age=TODAY.year - AGE.year #it wll calculate year of age irrespective of Birthday
            print(f"you are in {Current_age} now..!")
            Edate=datetime.strftime(AGE,"%d/%m/%Y") # strftime is convert into european date fromate
            print("In European date", Edate)
            break # once age is correctly calculated hen look will get stop its excutuin

            
    except ValueError:  # to handle error
        print("you have entered in wrong formate, please enter in MM/DD/YYYY formate")

   


