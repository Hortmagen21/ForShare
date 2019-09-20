import pickle

import psycopg2

database = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
cursor = database.cursor()
cursor.execute("SELECT * FROM databaseSQL WHERE name='max'")
row=cursor.fetchall()
print(len(row))