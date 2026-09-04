#Write a Python program to show method overloading by adding two numbers and three numbers using the same method name.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565010")
print("Practical-20")
class Addition:
    def add(self, a,b,c=0):
        return a + b + c
obj = Addition()
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("\n Sum of two numbers : ",obj.add(a,b))
c = int(input("Enter third number : "))
print("\n Sum of three numbers : ",obj.add(a,b,c))
