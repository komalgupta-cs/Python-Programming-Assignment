#Multiple Inheritance : Encryption + Authrntication -> SecureSystem
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-23_2")
class Encryption:
    def encrypt(self):
        print("Data is encrypted")

class Authentication:
    def authenticate(self):
        print("user authentication is performed")

class SecureSystem(Encryption, Authentication):
    def secure_data(self):
        print("System provides secure data access")

s = SecureSystem()
s.encrypt()
s.authenticate()
s.secure_data()
