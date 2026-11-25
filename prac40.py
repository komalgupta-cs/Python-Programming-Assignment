
# Python program to create a Bar Graph

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-40")

# Import matplotlib library
import matplotlib.pyplot as plt

# Define subjects and marks
subjects = ["Python", "DBMS", "CNS", "CLSC"]
marks = [85, 78, 92, 80]

# Create bar graph
plt.bar(subjects, marks)

# Add title and labels
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display bar graph
plt.show()
