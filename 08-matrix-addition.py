# Python program to add two matrix using array and function

print("\n Program :- MSc CS & CL")
print("\n Semester-1")
print("\n Name : Komal Gupta")
print("\n Enrollment : 92600565010")
print("\n Practical-8")

A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B=[[9,8,7],
   [6,5,4],
   [3,2,1]]

res=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        res[i][j] = A[i][j] + B[i][j]

print("\n Matrix after addition")

for row in res:
    print(row)
