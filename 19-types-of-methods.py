#Python program to demonstrate various types of methods
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565010")
print("Practical-19")
class Student:
    university = "Marwadi University"
    def __init__(self, name, enrollment_no, marks):
        self.name = name
        self.enrollment_no = enrollment_no
        self.marks = marks
    #Instance method
    def display_details(self):
        print("Student Name : ",self.name)
        print("Enrollment No. : ",self.enrollment_no)
        print("Marks : ",self.marks)
    #class method
    @classmethod
    def display_university(cls):
        print("University : ",cls.university)
    #Static method
    @staticmethod
    def check_result(marks):
        if marks >= 40:
            return "Pass"
        else:
            return "Fail"
#Creating an object
student1 = Student("Komal Gupta","150825",90)
#calling instance method
print("Instance Method")
student1.display_details()
#calling class method
print("Class Method")
Student.display_university()
#calling static method
print("Static Method")
result = Student.check_result(student1.marks)
print("Result : ",result)








        
