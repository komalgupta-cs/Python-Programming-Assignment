# Python program to check open ports using socket

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-48")

# Import socket module
import socket

# Specify target IP address
target = "127.0.0.1"

# Define port numbers
ports = [21, 22, 80, 443]

print("\nScanning Target:", target)

# Check each port
for port in ports:

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout
    s.settimeout(1)

    # Check port status
    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED")

    # Close socket
    s.close()

print("\nPort Scanning Completed.")
