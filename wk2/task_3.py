"""
Exercise 3 : Student Marks Processor (20 points)
Develop a program that:
1. Reads student marks data from a file (registration number, exam mark, coursework mark)
2. Computes overall marks using given weighting
3. Assigns grades based on specific rules
4. Creates a structured NumPy array
5. Sorts students by overall mark
6. Writes results to an output file
7. Displays grade statistics
8. Handles all errors gracefully
"""

# importing numpy for numerical array calculation
import numpy as np
# seting default value for exam and cOURSE WORK 
Exam=0.65
CourseW=0.35
# creting seperate variable for input and output fils
INF="C:\\Users\\DELL\\OneDrive\\Desktop\\internship\\Assignments\\wk\\Student.txt"
OUF="C:\\Users\\DELL\\OneDrive\\Desktop\\internship\\Assignments\\wk2\\Output.txt"

# this fumctions allows us to find the grade 
def Grade(m):
    if m>=80:
         return 'A'
    elif m>=65:
         return 'B'
    elif m>=50:
         return 'C'
    elif m>=40:
         return 'D'
    else:
         return 'F'


try:
    S=[]
    # openeing file 
    with open(INF,"r") as f:
        # getting data in file one by one
        for line in f:
            Reg_no,EM,CW=line.strip().split(",")
            EM = float(EM)
            CW = float(CW)
            # final marks calculation 
            Final_Marks=EM*Exam+CW*CourseW
            # checkng for grade 
            S_grade=Grade(Final_Marks)
            # adding all marks with grade and reg no into S LIST
            S.append((Reg_no,EM,CW,S_grade))
            #creating numpy array
        Student_array=np.array(S,dtype=[("R_NO","U5"),
                                            ("E","f"),
                                            ("C","f4"),
                                            ("Overall","f4"),
                                            ("G","U1")]
         )
        # sorting the array
    Student_array.sort(order="Overall")
    Student_array=Student_array[::-1] # in descending sort of array
    # writng data into output file
    with open(OUF,"w") as f:
         f.write("Ovrall perfomance")
         for i in Student_array:
            f.write(f"{i['R_NO']} {i['E']:.1f} {i['C']:.1f} {i['Overall']:.1f} {i['G']}\n")

    print("Grad statistics")
    grades = Student_array["G"]
    
    for g in ["A", "B", "C", "D", "F"]:
        print(f"Grade {g}: {list(grades).count(g)}")
    # exceptional handling with value type and file not found type    
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Invalid data in file.")
