# Python program to check files in a directory using os library

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-50")

# Import os library
import os

# Specify directory path
directory = "."

# Check whether directory exists
if os.path.exists(directory):

    print("\nFiles in the Current Directory:")

    # List directory contents
    items = os.listdir(directory)

    # Display files only
    for item in items:
        path = os.path.join(directory, item)

        if os.path.isfile(path):
            print(item)

else:
    print("Directory does not exist.")
