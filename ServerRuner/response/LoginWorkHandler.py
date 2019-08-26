from response.requestHandler import RequestHandler
import psycopg2
from pathlib import Path
import json
from response.ConnectingToDatabase import Connecter
class LoginHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"


    def checkSQLData(self,data):
        database=psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor=database.cursor()
        #cursor.execute("SELECT * FROM databaseSQL WHERE name='{}'".format(data["username"]))
        # row возвращает в кортежах столбец(DATApsycopg.py infa)
        self.setStatus(409)
        cursor.execute("SELECT * FROM databaseSQL WHERE name='{}'".format(data["username"]))
        for row in cursor.fetchall():
            if row[1]==data["username"] and row[2]==data["password"]:
                self.setStatus(200)
                data["gainId"]["id"]=row[0]
                break
        database.commit()
        cursor.close()
        database.close()
