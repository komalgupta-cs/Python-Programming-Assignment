
# Write a Python program to delete records from a MySQL table and display records.

print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-35")

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

# Delete records
sql = "DELETE FROM customers WHERE name = %s"
values = ("Amit",)

mycursor.execute(sql, values)
mydb.commit()

print("Records deleted successfully")

# Retrieve remaining records
mycursor.execute("SELECT * FROM customers")

# Display records
print("\nRemaining Customer Records:")

for record in mycursor.fetchall():
    print("Name:", record[0], "| City:", record[1])

# Close connection
mycursor.close()
mydb.close()
