from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'employees'

TABLES = {}
TABLES['employees'] = ("""
    CREATE TABLE `employees` (
      `emp_no` int(11) NOT NULL AUTO_INCREMENT,
      `birth_date` date NOT NULL,
      `first_name` varchar(14) NOT NULL,
      `last_name` varchar(16) NOT NULL,
      `gender` enum('M','F') NOT NULL,
      `hire_date` date NOT NULL,
      PRIMARY KEY (`emp_no`)
    ) ENGINE=InnoDB
""")

TABLES['departments'] = ("""
    CREATE TABLE `departments` (
      `dept_no` char(4) NOT NULL,
      `dept_name` varchar(40) NOT NULL,
      PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)
    ) ENGINE=InnoDB
""")

cnx = mysql.connector.connect(host = 'localhost',user='admin', password = 'admin')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()