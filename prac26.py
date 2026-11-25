#Write a python program to use try-except-else block
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-26")

try:
    attempts = int(input("Enter number of login attempts : "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("Login attempts recorded : ",attempts)
