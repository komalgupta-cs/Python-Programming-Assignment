
# Python program to create a Histogram

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-39")

# Import matplotlib library
import matplotlib.pyplot as plt

# Define student marks
marks = [45, 55, 60, 65, 70, 72, 75, 78, 80, 82,
         85, 88, 90, 92, 95, 68, 74, 79, 83, 87]

# Create histogram
plt.hist(marks, bins=5, edgecolor="black")

# Add title and labels
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

# Display histogram
plt.show()
