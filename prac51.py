# Python program to check whether an IP address is UP or DOWN using Ping

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-51")

# Import subprocess module
import subprocess

# Specify target IP address
ip = "10.0.2.15"

# Display scanning information
print("\nChecking IP Address:", ip)

# Execute ping command
result = subprocess.run(
    ["ping", "-c", "1", "-W", "2", ip],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# Check IP status
if result.returncode == 0:
    print("IP Address", ip, "is UP")
else:
    print("IP Address", ip, "is DOWN")
