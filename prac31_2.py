#Import the regular expression module
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-31")
import re

#Searching for a pattern
text = "Cybersecurity Lab 2026"

if re.search(r'\d', text):
    print("1. The string contains a number.")
else:
    print("1. No number found in the string.")

#extracting emails
text_with_emails = "Contact us at support@cyberlab.com or admin"

#Pattern to find valid email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]*'
emails = re.findall(email_pattern, text_with_emails)
print("2. Extracted Emails : ",emails)

#validating a phone number
phone = "9874563210"

#pattern for 10-digit phone number
if re.fullmatch(r'\d{10}', phone):
    print("3. Valid phone number.")
else:
    print("3. Invalid phone number.")

#Finding capitalized words
sentence = "Python is fun and important"

#find all words starting with capital letters
capital_word = re.findall(r'\b[A-Z][a-z]*\b',sentence)
print("4. Words starting with capital letters : ", capital_word)

#Replacing digits
text_with_digits = "Server123 has IP456"
#Replace all digits with '#'
replaced_text = re.sub(r'\d','#',text_with_digits)
print("5. Text after replacing digits :",replaced_text)
