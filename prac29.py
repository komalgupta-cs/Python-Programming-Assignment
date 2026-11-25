#Python program to demonstrate file handling

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-29")
#Create and write data to a file
file = open("demo.txt","w")
file.write("Cyber security lab \n")
file.write("MSc Cyber Security and Cyber Law \n")
file.write("File handling is important for managing security log")
file.close()

#Read data from the file
file = open("demo.txt","r")
data = file.read()
print("File Contents : ")
print(data)
file.close()

#Append new data to the file
file = open("demo.txt","a")
file.write("New security event recorded")
file.close()

#Read the updated file
file = open("demo.txt","r")
print("Updated file contents : ")
print(file.read())
file.close()
