from response.requestHandler import RequestHandler
import psycopg2
from pathlib import Path
import json
class LoginHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"
    def check(self, data):
        path = Path('ServerRuner/response/DataBase.json')
        a = json.loads(path.read_text(encoding='utf-8'))
        contactLen = len(a["data"])
        isDuplicate = False
        i = 0
        while i<contactLen and isDuplicate==False:
            print(a["data"][i]["username"])
            print(a["data"][i]["password"])
            if a["data"][i]["username"]==data["username"] and a["data"][i]["password"]==data["password"]:
                self.setStatus(200)
                isDuplicate = True
            i = i + 1
        if isDuplicate==False:
            self.setStatus(404)
    def checkSQLData(self,data):
        database=psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor=database.cursor()
        cursor.execute("SELECT * FROM acctester")
        # row возвращает в кортежах столбец(DATApsycopg.py infa)
        for row in cursor.fetchall():
            if row[1]==data["username"] and row[2]==data["password"]:
                self.setStatus(200)
            else:
                self.setStatus(409)
        database.commit()
        cursor.close()
        database.close()
