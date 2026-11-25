
# Python program to perform a WHOIS lookup for a given domain name

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-42")

# Import WHOIS module
import whois

# Specify domain name
domain = "google.com"

# Perform WHOIS lookup
result = whois.whois(domain)

# Display WHOIS information
print("\nWHOIS Information:")
print("Domain Name:", result.domain_name)
print("Registrar:", result.registrar)
print("Creation Date:", result.creation_date)
print("Expiration Date:", result.expiration_date)
print("Name Servers:", result.name_servers)
print("Domain Status:", result.status)
