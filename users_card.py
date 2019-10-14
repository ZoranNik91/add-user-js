'''
1   create database for users - First Name, Last Name, email, password, ID (random)
2   save user on database, give a ID to card 
3   the card scanner must recognise user by ID, door open if is valid, not if its Invalid   

Napraviti program koji će zabilježavat vrijeme dolaska i odlaska sa posla te pohranjivat u bazu podataka
dodir kartice na scenner

'''
import mysql.connector as MC
import sys
import random

if len(sys.argv) < 4:
    sys.exit("Invalid number of arguments. Three expected (username, email, password)")


if len(sys.argv[3]) > 32 or len(sys.argv[3]) < 8:
    sys.exit("Invalid password length")

ID = random.getrandbits(12)
print(ID)

db = MC.connect(host='localhost', database='employees',
                user='admin', password='admin')

cursor = db.cursor()

add_user = ("INSERT INTO employee (username, email, password, ID) VALUES (%s, %s, %s,")
data_user = (sys.argv[1], sys.argv[2], sys.argv[3])
cursor.execute(add_user, data_user)

db.commit()
cursor.close() 
db.close()