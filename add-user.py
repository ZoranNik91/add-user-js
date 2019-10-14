import mysql.connector as MC
import sys

if len(sys.argv) < 4:
    sys.exit("Invalid number of arguments. Three expected (username, email, password)")


if len(sys.argv[3]) > 32 or len(sys.argv[3]) < 8:
    sys.exit("Invalid password length")

db = MC.connect(host='localhost', database='jpp-sql',
                user='admin', password='admin')
cursor = db.cursor()
add_user = ("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)")
data_user = (sys.argv[1], sys.argv[2], sys.argv[3])
# Insert new employee
cursor.execute(add_user, data_user)
# Make sure data is committed to the database
db.commit()
cursor.close()
db.close()
