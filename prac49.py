# Python program to generate hash values using hashlib

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-49")

# Import hashlib library
import hashlib

# Input string
text = "Cyber Security"

# Convert string into bytes
data = text.encode()

# Generate MD5 hash
md5_hash = hashlib.md5(data).hexdigest()

# Generate SHA-1 hash
sha1_hash = hashlib.sha1(data).hexdigest()

# Generate SHA-256 hash
sha256_hash = hashlib.sha256(data).hexdigest()

# Display hash values
print("\nOriginal String:", text)
print("\nMD5 Hash:", md5_hash)
print("SHA-1 Hash:", sha1_hash)
print("SHA-256 Hash:", sha256_hash)
