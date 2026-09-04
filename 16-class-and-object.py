#Python Program to demonstrate the use of class
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-16")
class MyNewClass:
    """This class demonstrates the creation of objects"""
#instance attribute
    num=100
    #instance method
    def hello(self):
        print("\n Hello World !")
#creating object ofo MyNewClass
obj = MyNewClass()
print(obj.num)
obj.hello()
print(MyNewClass.__doc__)
