
# Python program to demonstrate the use of DataFrames in Python

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-36")

# Import pandas library
import pandas as pd

# Create a dictionary containing student data
data = {
    "Name": ["Vashisth", "Rahul", "Priya", "Amit"],
    "Course": ["MSc CS & CL", "MSc CS & CL", "MSc CS & CL", "MSc CS & CL"],
    "City": ["Jamnagar", "Ahmedabad", "Rajkot", "Surat"],
    "Marks": [85, 78, 92, 80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("\nStudent DataFrame:")
print(df)

# Display specific column
print("\nStudent Names:")
print(df["Name"])

# Display first two records
print("\nFirst Two Records:")
print(df.head(2))
