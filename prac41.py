
# Python program to create a Line Graph

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-41")

# Import matplotlib library
import matplotlib.pyplot as plt

# Define subjects and marks
subjects = ["Python", "DBMS", "CNS", "CLSC"]
marks = [85, 78, 92, 80]

# Create line graph
plt.plot(subjects, marks, marker='o', linestyle='-')

# Add title and labels
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display line graph
plt.show()
