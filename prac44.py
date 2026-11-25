
# Python program to display the domain registrar name using WHOIS

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-44")

# Import WHOIS module
import whois

# Specify domain name
domain = "tryhack.com"

# Perform WHOIS lookup
result = whois.whois(domain)

# Display registrar name
print("\nDomain Name:", domain)
print("Registrar Name:", result.registrar)
