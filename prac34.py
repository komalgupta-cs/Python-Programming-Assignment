# Write a Python program to update records in a MySQL table and display records.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-34")

import mysql.connector

# Connect Python with MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marwadi01"
)

print("Database Connected Successfully")

# Create cursor
mycursor = mydb.cursor()

# Update a record
sql = "UPDATE customers SET city = %s WHERE name = %s"
values = ("Jamnagar", "Vashisth")

mycursor.execute(sql, values)
mydb.commit()

print("Record updated successfully")

# Retrieve and display records
mycursor.execute("SELECT * FROM customers")

print("\nUpdated Customer Records:")

for record in mycursor.fetchall():
    print("Name:", record[0], "| City:", record[1])

# Close connection
mycursor.close()
mydb.close()
