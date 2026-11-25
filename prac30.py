#Python program to demonstrate the use of various mode of file
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-30")
#r+ = Read and write mode
file = open("demo.txt","r+")
print("r+ Mode :")
print(file.read())
file.write("Addtional data using r+ Mode. \n")
file.close()

#w+ = Write and read mode 
file = open("demo.txt","w+")
file.write("Security Report \n")
file.write("Threat analysis completed. \n")
file.seek(0)
print("w+ Mode:")
print(file.read())
file.close()

#a+ = Append and read mode
file = open("demo.txt","a+")
file.write("Security Report updated\n")
file.seek(0)
print("a+ Mode:")
print(file.read())
file.close()
