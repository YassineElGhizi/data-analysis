import pymysql
import pandas as pd

def init():
    mydb = pymysql.connect(
        host="127.0.0.1",
        port=4306,
        user="root",
        password="example",
    )
    mycursor = mydb.cursor()

    try:
        mycursor.execute('create database data_analytics')
    except Exception as e:
        print(e)

    try:
        table = 'year int,' \
                'city varchar(100),' \
                'country varchar(100),' \
                'avg_temp double(13 , 10)'
        sql = 'create table data_analytics.city_data (' + table +')'
        mycursor.execute(sql)
    except Exception as e:
        print(e)

def csv_to_mysql():
    mydb = pymysql.connect(
        host="127.0.0.1",
        port=4306,
        user="root",
        password="example",
        database= "data_analytics"
    )
    mycursor = mydb.cursor()

    # Import CSV
    data = pd.read_csv (r'.\city_data.csv')
    df = pd.DataFrame(data, columns= ['year','city','country','avg_temp'])


    sql = "insert into city_data (year , city , country , avg_temp) values (%s,%s,%s,%s)"
    for l in df.itertuples():
        if str(l.avg_temp) == 'nan':
            val = ( str(l.year) , l.city , l.country, None )
        else:
            val = ( str(l.year) , l.city , l.country, str(l.avg_temp))
        print( val )
        mycursor.execute(sql, val)
        mydb.commit()


if __name__ == "__main__":
    init()
    csv_to_mysql()