import pickle
import selenium.webdriver
import psycopg2
a=409
database=psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
cursor=database.cursor()
        #cursor.execute("SELECT * FROM databaseSQL WHERE name='{}'".format(data["username"]))
        # row возвращает в кортежах столбец(DATApsycopg.py infa)
cursor.execute("SELECT * FROM databaseSQL WHERE name='{}'".format("max21"))
for row in cursor.fetchall():
    print(row)
    print(row[1])
    print(row[2])
    if row[1]=="max21" and row[2]=="21042002":
        a=200
        break
        database.commit()
        cursor.close()
        database.close()
print(a)