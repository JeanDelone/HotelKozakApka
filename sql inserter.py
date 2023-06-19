import mysql.connector
import random

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hotel"
)

names1 = ["John", "Jan", "Monika", "Patryk", "Karol"]
names2 = ["Mesa", "Border", "Kalino", "Bossowski", "Essowski"]

mycursor = db.cursor()
mycursor.execute("ALTER TABLE guests MODIFY guest_id INT AUTO_INCREMENT PRIMARY KEY")

# Create guests table if it doesn't exist
# mycursor.execute("CREATE TABLE IF NOT EXISTS guests (guest_id INT AUTO_INCREMENT PRIMARY KEY, room_id INT, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, check_in_date DATE, check_out_date DATE, FOREIGN KEY (room_id) REFERENCES rooms (room_id))")

# # Insert guests
# for i in range(10):
#     room_id = i  # Replace with the actual room ID
#     first_name = random.choice(names1)
#     last_name = random.choice(names2)
#     lower_random = random.randint(1, 10)
#     upper_random = random.randint(lower_random, 20)
#     check_in_date = f"2023-07-{lower_random}"
#     check_out_date = f"2023-07-{upper_random}"
#     insert_query = "INSERT INTO guests (room_id, first_name, last_name, check_in_date, check_out_date) VALUES (%s, %s, %s, %s, %s)"
#     data = (room_id, first_name, last_name, check_in_date, check_out_date)
#     mycursor.execute(insert_query, data)

db.commit()

# Close the cursor and the database connection
mycursor.close()
db.close()
