import pymysql
import csv

mydb = pymysql.connect(
    host="127.0.0.1",
    port=4306,
    user="root",
    password="example",
    database="data_analytics"
)
mycursor = mydb.cursor()
sql = "select * from city_data where city = %s"
val = ( 'casablanca' ,)
mycursor.execute(sql , val)
myresult = mycursor.fetchall()

with open('morocco.csv', 'w', newline='') as f:
    fieldnames = ['year','city','country','avg_temp']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for l in myresult:
        writer.writerow({'year': l[0], 'city': l[1] , 'country' : l[2] , 'avg_temp' : l[3]})
    f.close()

