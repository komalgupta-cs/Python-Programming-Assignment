#Multilevel Inheritance : Security tool -> NetworkSecurity -> Firewall
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-23_1")
class Security:
    def protect(self):
        print("System protection is enabled")
class NetworkSecurity(Security):
    def monitor_network(self):
        print("Network traffic is monitored")
class Firewall(NetworkSecurity):
    def block_traffic(self):
        print("Malicious traffic is blocked")

f = Firewall()
f.protect()
f.monitor_network()
f.block_traffic()
