## 2. Connecting to Postgres ##

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
conn.close()

## 3. Interacting with the database ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("Select * from users")
users = cur.fetchall()
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute(
"""
    CREATE TABLE users (
        id integer PRIMARY KEY, 
        email text, 
        name text, 
        address text
    );
""")

## 6. The commit method ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
query_string = """
    CREATE TABLE users(
        id integer PRIMARY KEY, 
        email text,
        name text,
        address text
    );
"""

curr = conn.cursor()
curr.execute(query_string)
conn.commit()
conn.close()

## 7. Local state and commits ##

import psycopg2
conn1 = psycopg2.connect("dbname=dq user=dq")
cur1 = conn1.cursor()
cur1.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, 'alice@dataquest.io', 'Alice', '99 Fake Street'))
conn2 = psycopg2.connect("dbname=dq user=dq")
cur2 = conn2.cursor()
# add your code here
cur1.execute("select * from users;")
view1_before = cur1.fetchall()
cur2.execute("select * from users;")
view2_before = cur2.fetchall()
conn1.commit()

cur2.execute("select * from users;")
view2_after = cur2.fetchall()

             

## 9. Inserting data into a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
curr = conn.cursor()
curr.execute("insert into users values(%s, %s, %s, %s);", (2, "pranshu1921@gmail.com", "Pranshu", "75, St Alphonsus St"))
conn.commit()
conn.close()

## 10. Copying the data ##

import psycopg2
import csv
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        cur.execute("insert into users values(%s, %s, %s, %s);", row)
conn.commit()
conn.close()
        
        