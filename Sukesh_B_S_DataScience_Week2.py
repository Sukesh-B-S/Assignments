
# Task 1 :Basic Operations

"""
Write a Python program that:
1. Accepts two integer inputs from the user.
2. Performs the following operations using arithmetic operators:
○ Addition, Subtraction, Multiplication, Division, Modulus, and Exponentiation.
3. Prints the results in a well-formatted way using f-strings.

"""
# asking user to enter 2 numbers 

A=int(input("Enter the first number\n")) 
B=int(input("Enter the second number\n"))

# printing Addition of numbers. f is used for formated output
print(f"Addition of {A} and {B} is : ",(A+B))

# printing Substaracton of numbers.  
print(f"Substraction of {A} and {B} is : ",(A-B))

# printing multiplication of numbers.  
print(f"Multiplication of {A} and {B} is : ",(A*B))

# printing division of numbers.  
print(f"Division between {A} and {B} is : ",(A/B))

# printing modulus  of numbers.  
print(f"Remailner of {A} and {B} is : ",(A%B))

# printing exponentioal of numbers.  
print(f"{A} power of  {B} is : ",(A**B))

print("Calculation done...!")

#==============================================================================================

#Task 2: Working with Lists and Arrays

"""
1. Create a list containing at least 10 numbers.
2. Perform the following:
○ Print the length of the list.
○ Find the maximum and minimum value.
○ Add a new element to the list and remove one element.
○ Sort the list in ascending and descending order.
3. Convert the list into a NumPy array and calculate:
○ Mean, Median, and Standard Deviation.
"""
# creating list of numbers 

L=[2,4,6,-4,5,1,8]

# Print the length of the list.
print("Length of list L : ", len(L)) # len() is used to get lenght of list

# Find the maximum and minimum value.
print("Maximum value among List L :",max(L) )# max() is used to get large number in List
print("Manimum value among List L :",min(L) )# min() is used to get smallrge number in List

# Add a new element to the list and remove one element.

L.append(9) # append will add a number into list ar the end 
print(L)   # After adding into list
L.pop(1) # Remove element by index
L.remove(-4) # Remove element by value 
print(L) # After removal from list

#Sort the list in ascending and descending order.

L.sort()
print("Ascending order",L) # Print in ascending order
L.sort(reverse=True) 
print("descendingen order",L)# Print in descending order

#Convert the list into a NumPy array and calculate:

# we need to import package called  numpy to deal with numpy array
import numpy as numpython
l=numpython.array(L) # storring in l array
print("array : ", l)    # printing numpy array

# Mean, Median, and Standard Deviation.
print("mean of array : ",numpython.mean(l)) #numpython.mean() willl find mean value of array
print("median of array l: ",numpython.median(l))#numpython.median () for meadian o array
print("standard deviation : ", numpython.std(l)) # #numpython.std()  for standard deviation


#==================================================================================================

#Task 3: Dictionaries and Sets

"""
1. Create a dictionary named student with keys: name, age, course, marks.
2. Print each key-value pair using a loop.
3. Add a new key called grade with a value of your choice.
4. Create a set of unique courses (e.g., {“Python”, “Data Science”, “AI”, “Python”}) and display it.
5. Perform set operations — union, intersection, and difference — between two sets of sample data.
"""
# creating dictionary 


student={"Name":"Sukesh B S", "Age": 20, "course":"BTech","Marks": 70}
for k in student:
    print(k ," : ",student[k]) # print both key values pairs 

# Add a new key called grade with a value of your choice.

student.update({"grade":"12th"}) # adding value into dictionary
print("updated dictionary :",student.items()) # printing dictionary 

# Create a set of unique courses (e.g., {“Python”, “Data Science”, “AI”, “Python”}) and display it.

Uniq_courses={"science","phydics","maths"," english","science"}
print(Uniq_courses) # printing sets where it will cut duplicates 

# Perform set operations — union, intersection, and difference — between two sets of sample data.

S1={2,6,7,3,5,8}
S2={5,7,3,7,0,8}
print(S1.union(S2))# unnion of two sets combined 
print(S1.intersection(S2)) # common vales in bith sets will gt print
print(S1.difference(S2)) # diffrence btw S1 from S2

#===========================================================================================

#File Handling
"""
1. Create a text file named student_data.txt.
2. Write the following information into the file (name, course, and marks of at least 5 students).
3. Read the file and display only those students whose marks are above 75.
"""

with open("student_data.txt","w") as f: #  for writng 
    f.write("Manja , AI , 56\n")     # wrinting content into file
    f.write("Rajappa,ML,43\n")
    f.write("Anupama,DS,86\n")
    f.write("Jhon cena,ML,94\n")
    f.write("Gouramma,AI,90\n")

with open("student_data.txt", "r") as f:  # for reading 
    for line in f:                      # Going through file content line by line
     name,course,marks=line.split(",") # storing name, course, and marks values , split() can splits ines basd on 
     print(name,course,marks)  # dislay content based on parameters
     if int(marks)>75:          # checking marks for >75 
        print("More than 75 : ",name, course)  # printing the name and course who scored >75

#+===============================END=======================================================================================