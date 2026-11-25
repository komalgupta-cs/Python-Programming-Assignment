#Write a Python program to create a table, insert records, retrieve and display records from a table.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-33")
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

# Create table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    name VARCHAR(255),
    city VARCHAR(255)
)
""")

print("Table created successfully")

# Insert records
sql = "INSERT INTO customers (name, city) VALUES (%s, %s)"

records = [
    ("Vashisth", "Mumbai"),
    ("Rahul", "Ahmedabad"),
    ("Priya", "Rajkot"),
    ("Amit", "Surat")
]

mycursor.executemany(sql, records)
mydb.commit()

print("Records inserted successfully")

# Retrieve records
mycursor.execute("SELECT * FROM customers")

# Display records
print("\nCustomer Records:")

for record in mycursor.fetchall():
    print("Name:", record[0], "| City:", record[1])

# Close connection
mycursor.close()
mydb.close()
