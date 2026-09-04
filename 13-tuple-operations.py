#Python Programs to demonstrate the use of dictionary and various functions of it
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-13")

#Dictionary and its function
dict = {'Name' : 'Komal', 'Age' : '20', 'Class' : 'CL & CS'}
print("dict['Name'] : ",dict['Name'])
print("dict['Age'] : ",dict['Age'])
print("dict['Class'] : ",dict['Class'])
#---------------------------------------------------------------------------------

print("After updating values")
dict['Age'] = 21
dict['University'] = "MU"
print("dict['Age'] : ",dict['Age'])
print("dict['University'] : ",dict['University'])
#----------------------------------------------------------------------------------

print("After deleting name : ")
del dict['Name']
print("Values in dict : ",dict)
#----------------------------------------------------------------------------------

print("Remove all entries in dict : ")
dict.clear()
print("Dict : ",dict)
#----------------------------------------------------------------------------------

print("Delete entire dictionary : ")
del dict
print("Dict : ",dict)
#----------------------------------------------------------------------------------

print("dict['Age'] : ",dict['Age'])
#----------------------------------------------------------------------------------

dict1 = {'Name' : 'Komal', 'Age' : '20', 'Name' : 'Rita'}
print("dict1['Name'] : ",dict1['Name'])
#----------------------------------------------------------------------------------

dict1['Name']
dict1.get('Age',0)
