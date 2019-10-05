from response.requestHandler import RequestHandler
import psycopg2
from pathlib import Path
import json
class InputHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"

    def takeSQLData(self, data):
        self.setStatus(200)
        database = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM databaseSQL WHERE id='{}'".format(int(data["id"])))
        #data["getname"]["name"]=cursor.fetchall()[0][1]
        data['name']=cursor.fetchall()[0][1]
        self.contents=data['name'][0]
        database.commit()
        cursor.close()
        database.close()