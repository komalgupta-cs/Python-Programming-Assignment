#Write a python program to use try-except-finally block
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-27")

try:
    attempts = int(input("Enter number of login attempts : "))
    print("Login attempts : ",attempts)
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Security check completed")
