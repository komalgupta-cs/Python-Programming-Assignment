#Hierarchical Inheritance : Security System -> IDS and IPS
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-23_3")
class SecuritySystem:
    def monitor(self):
        print("Network is bring monitored")

class IDS(SecuritySystem):
    def detect(self):
        print("IDS detects suspicious activity")

class IPS(SecuritySystem):
    def prevent(self):
        print("IPS prevents malicious activity")

i = IDS()
p = IPS()

i.monitor()
i.detect()
p.prevent()
