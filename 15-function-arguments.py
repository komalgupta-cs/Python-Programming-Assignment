#Python Programs to demonstrate use of various arguments which can be passed to functions
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-15")

#Positional Arguments
print("\n Positional Argument")
def student(name,age):
    print("Name : ",name)
    print("Age : ",age)
student("Komal",20)
#Keyword Arguments
print("\n Keyword Argument")
student(age=21, name="Rita")
#Default Arguments
print("\n Default Argument")
def greet(name="Student"):
    print("Hello",name)
greet()
greet("Komal")
#Variable-length Argument
print("\n Variable - length Argument")
def total(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    print("Total = ",sum)
total(10,20)
total(10,20,30,40,50)
