#Python program to demonstrate the use of methods
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-18")
class Student:
    #Method to display student details
    def display_details(self,name,enrollment_no,department):
        print("University : Marwadi University")
        print("Student Name : ",name)
        print("Enrollment No. :- ",enrollment_no)
        print("Department : ",department)
    #Method to calculate total marks
    def calculate_total(self,marks1,marks2,marks3):
        total = marks1 + marks2 + marks3
        return total
#Create an object of the class
student = Student()
#calling the display_details() method
student.display_details("Komal Gupta","150825","FoCA")
#Calling the calculate_total() method
total = student.calculate_total(85,90,76)
print("Total Marks : ",total)
