#Python program to create a function(Make your own assumptions)
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-14")
def check_number(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter your number : "))
result=check_number(num)
print("The entered number is :",result)
