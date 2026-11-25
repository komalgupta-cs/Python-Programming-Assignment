#Write a python program to handle invalid input entered by the user
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-25")

try:
    number = int(input("Enter a number : "))
    print("You entered : ", number)
except ValueError:
    print("Error : Invalid input. Please enter a number.")
