import psycopg2
import os
from ServerRuner.response.ConnectingToDatabase import Connecter
#database=psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
#cursor=database.cursor()

#cursor.execute("CREATE TABLE databaseSQL (id serial, name varchar PRIMARY KEY, password varchar);")
#cursor.execute("INSERT INTO acctester2 (name,password) VALUES(%s, %s)",("alexer","15"))
#cursor.execute("SELECT * FROM acctester")
#print(cursor.fetchall()[0][2])
#for row in cursor.fetchall():
    #print(row)
    #print(row[0])
    #print(type(row[0]))
split_path=os.path.splitext("http://localhost:1000/?id")
a=os.path.split(split_path[0])
pather="http://localhost:1000/login"
if a[1][0] == "?":
    print("ok")
    pather = a[0]+"/"
print(pather,"pather")
print(os.path.split(pather),"split pather")

print(split_path,"splitpath")
print(a,"a")


#curser.execute("SELECT * FROM test;")
#curser.fetchone()
#("a",101)
#database.commit()
#cursor.close()
#database.close()
