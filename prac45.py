
# Python program to display the domain creation date using WHOIS

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-45")

# Import WHOIS module
import whois

# Specify domain name
domain = "chatgpt.com"

# Perform WHOIS lookup
result = whois.whois(domain)

# Display domain creation date
print("\nDomain Name:", domain)
print("Creation Date:", result.creation_date)
