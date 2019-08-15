from response.requestHandler import RequestHandler
from pathlib import Path
import json
import psycopg2




class RegistrationHandler(RequestHandler):
    def __init__(self):#создали конструктор
        super().__init__()#err in ajax
        self.contentType = "application/json"
    def checkandadd(self,data):
        #with open("ServerRuner/response/DataBase.json")as js_database:
        path=Path('ServerRuner/response/DataBase.json')
        print(path)
        a=json.loads(path.read_text(encoding='utf-8'))
        contactLen=len(a["data"])
        isDuplicate = False
        i=0
        print(contactLen,"длина массива")
        while i<contactLen and isDuplicate==False:
            if a["data"][i]["username"]==data["username"]:
                self.setStatus(409)
                isDuplicate=True
            i=i+1
            print(i,'значение i')
        print(isDuplicate,"ми вышли с массива")
        if isDuplicate==False:
            self.setStatus(200)
            a["data"].append({'username':data["username"],'password':data["password"]})
            path.write_text(json.dumps(a),encoding='utf-8')
    def checkSQLData(self,data):
        database=psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor=database.cursor()

        try:
            cursor.execute("INSERT INTO acctester (id,name,password) VALUES(%s,%s, %s)", (1,data["username"], data["password"]))
        except:
            print("ИСКЛЮЧЕНИЕ!!!!!!!!!!")
            self.setStatus(409)
        else:
            self.setStatus(200)

        cursor.execute("SELECT * FROM test;")
        cursor.fetchone()
        (1,data["username"], data["password"])
        database.commit()
        cursor.close()
        database.close()

