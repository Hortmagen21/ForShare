from response.requestHandler import RequestHandler
from pathlib import Path
import json
import psycopg2
from response.ConnectingToDatabase import Connecter
class RegistrationHandler(RequestHandler):
    def __init__(self):#создали конструктор
        super().__init__()#err in ajax
        self.contentType = "application/json"
    def checkSQLData(self,data):
        database = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor = database.cursor()#fix ConnectinDatabase
        try:
            cursor.execute("INSERT INTO acctester (id,name,password) VALUES(%s,%s, %s)", (1,data["username"], data["password"]))
        except:
            print("ИСКЛЮЧЕНИЕ!!!!!!!!!!")
            self.setStatus(409)
        else:
            self.setStatus(200)
        database.commit()
        cursor.close()
        database.close()

