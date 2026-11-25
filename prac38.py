
# Python program to create a Pie Chart

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-38")

# Import matplotlib library
import matplotlib.pyplot as plt

# Define data
subjects = ["Python", "DBMS", "CNS", "CLSC"]
marks = [85, 78, 92, 80]

# Create pie chart
plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)

# Add title
plt.title("Subject-wise Marks Distribution")

# Display pie chart
plt.show()
