#import modules
import csv
import pandas as pd
import mysql.connector
dbconn = mysql.connector.connect(host="localhost",port=3306,password="",
                             user="root", database="pollution-db2")
mycursor=dbconn.cursor()
#print(dbconn)

#check server connection
if (dbconn):
    print("Successfully connected to server")
else:
    print(" Cannot connect to server")

### sql statement 
mycursor.execute("SELECT * FROM readings ORDER BY ReadingsID LIMIT 100")

### Execute and output 100 inserts
myresult = mycursor.fetchall()
lines = ""
for x in myresult:
    lines +=   str(x) +"\n" 
print(lines)

# write output to file

f = open("insert-100.sql", "w")
#f.write(str(myresult))
f.write(lines)

f.close()
