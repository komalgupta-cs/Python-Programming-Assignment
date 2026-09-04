#Python Programs to demonstrate use of tuple and various functions of it
print("Program :- MSc CS & CL Semester-1")
print("Name : Komal Gupta")
print("Enrollment : 92600565010")
print("Practical-12")

tup1 = ('physics','chemistry',1917,2000)
tup2 = (1,2,3,4,5,6)
print("tup1[0] : ",tup1[0])
print("tup2[1:5] : ",tup2[1:5])
#----------------------------------------------------------------------------------

tupl1 = (2,34.56)
tupl2 = ('abc','xyz')
tupl3 = tupl1 + tupl2
print("Concatenation : ",tupl3)
#---------------------------------------------------------------------------------

tup = ('physics','chemistry',1917,2000);
tu = "Hey !"
tu4 = (1,2,3)
print("Length of tuple : ",len(tup))
print("Repetiton : ",tu*4)
print("Membership : ", 1 in tu4)
print("Iteration : ")
for x in tu4:
    print(x)
#----------------------------------------------------------------------------------

print("Original Value : ",tup2)
print("Index Value : ",tup2[5])
print("Negative Count : ",tup2[-1])
print("Slicing : ",tup2[1:5])
