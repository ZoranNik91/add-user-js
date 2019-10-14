# from __future__ import print_function
import mysql.connector as MC
import sys
from datetime import time
from datetime import datetime
import json


# Global variables
is_in = 1
# Connect to DB and set cursor
db = MC.connect(host='localhost', database='employees', user='admin', password='admin')
cursor = db.cursor()

if len(sys.argv) == 2:
    date_input = sys.argv[1]

    #cursor.execute(f"SELECT user_id FROM times WHERE time BETWEEN '{date_input} 00:00:00' AND '{date_input} 23:59:59'")
    cursor.execute(f"""
            SELECT name,surname,times.time FROM users
            JOIN times ON times.user_id = users.id
            WHERE time BETWEEN '{date_input} 00:00:00' AND '{date_input} 23:59:59'
            ORDER BY users.name
        """)
    
    rows = cursor.fetchall()

    res = []
    for row in rows:
        dateTime = row[2]
        formattedTime = dateTime.strftime("%H:%M:%S")
        formattedDate = dateTime.strftime("%Y-%m-%d")
        obj = {
            "name": row[0],
            "surname": row[1],
            "time": formattedTime,
            "date": formattedDate
        }
        # ti = time.format(time(dateTime.hour, dateTime.minute, dateTime.second))
        res.append(obj)
        
    print(json.dumps(res, indent=4, sort_keys=True))

else:

    card_id = input("Your ID: ")

    cursor.execute(f"SELECT * FROM users WHERE card_id = {card_id}")
    row = cursor.fetchone()

    # Checks if we have user or not, if not posibility to create on
    if (row == None):

        print("User doesnt exist!")
        print("Would you like to create a user ? (y/n): ", end = '')
        answer = input()
        if (answer == 'y'):
            print("User created")
            name = input("Name: ")
            surname = input("Surname: ")
            email = input("email: ")
            phone = input("Phone number: ")
            
            new_query = """
            INSERT INTO users (name, surname, email, phone, card_id) 
            VALUES (%s, %s, %s, %s, %s)
            """
            query = (name, surname, email, phone, card_id)
            cursor.execute(new_query, query)
            print(f"User {name} {surname} was created!")
            db.commit()

    # if the user exists    
    else:
        cursor.execute("SELECT * FROM times WHERE user_id = {}".format(row[0]))
        rows =  cursor.fetchall()

        # check if we have any record of user_id in times table (cursor.rowcount == 0)
        if (cursor.rowcount == 0):
            is_in = 1
            print(f"Welcome user {row[1]}. ", end='')
        # Check if user has entered or is leaving (cursor.rowcount %2 = 0 or 1)
        else:
            is_in = (cursor.rowcount + 1) % 2
            print(f"{'Signed in' if is_in else 'Signed out'}", end='')
            
        # Save new record
        new_query = "INSERT INTO times (is_in, user_id) VALUES (%s, %s)"
        query = (is_in, row[0])
        cursor.execute(new_query, query)
        db.commit()

cursor.close() 
db.close()