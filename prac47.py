# Python program to detect email addresses using Regular Expressions

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-47")

# Import re module
import re

# Sample text containing email addresses
text = """
Contact us at support@cyberlab.com
For queries, email admin@gmail.com
Invalid email: user@com
"""

# Define regular expression pattern
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display detected email addresses
print("\nDetected Email Addresses:")

for email in emails:
    print(email)

print("\nTotal Emails Found:", len(emails))
