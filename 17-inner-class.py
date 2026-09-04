#Python Program to demonstrate the use of class
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-17")
#Outer class
class University:
    def __init__(self,university_name):
        self.university_name = university_name
    #Inner class
    class student:
        def __init__(self,name,enrollment_no,department):
            self.name = name
            self.enrollment_no = enrollment_no
            self.department = department
        def display(self):
            print("Student Name : ",self.name)
            print("Enrollment No.: ",self.enrollment_no)
            print("Department : ",self.department)
#Create an object of the outer class
univ = University("Marwadi University")
#Create an object of the inner class
stud = univ.student("Komal Gupta", "150825", "FoCA")
#Display student details
print("University : ",univ.university_name)
stud.display()













            
