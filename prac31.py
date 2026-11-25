#searching for a pattern 
import re
text = "Cybersecurity Lab 2026"
if re.search(r"\d",text):
    print("1. The string contains a number")
else:
    print("1. No nummber found in the string")

#Extracting 
