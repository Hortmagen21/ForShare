import pickle
from urllib.parse import urlparse
import psycopg2

#atabase = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
#ursor = database.cursor()
#ursor.execute("SELECT * FROM databaseSQL WHERE name='max'")
#ow=cursor.fetchall()
#rint(len(row))
a='https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Statements/try...catch'
b=urlparse(a)
print(b)
