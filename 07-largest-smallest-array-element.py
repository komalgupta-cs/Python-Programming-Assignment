# Python program to print the largest element and smallest element in an array

print("\n Program :- MSc CS & CL")
print("\n Semester-1")
print("\n Name : Komal Gupta")
print("\n Enrollment : 92600565010")
print("\n Practical-7")

arr=[15,20,25,30,10]

largest=arr[0]
smallest=arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]

    if arr[i]<smallest:
        smallest=arr[i]

print("\n Elements of array are ",arr)

print("\n Largest Value is ",largest)
print("\n Smallest Value is ",smallest)
