
# Python program to accept a domain name and display basic WHOIS information

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-43")

# Import WHOIS module
import whois

# Accept domain name from user
domain = input("Enter Domain Name: ")

# Perform WHOIS lookup
result = whois.whois(domain)

# Display basic WHOIS information
print("\nBasic WHOIS Information:")
print("Domain Name:", result.domain_name)
print("Registrar:", result.registrar)
print("Creation Date:", result.creation_date)
print("Expiration Date:", result.expiration_date)
print("Name Servers:", result.name_servers)
print("Domain Status:", result.status)
