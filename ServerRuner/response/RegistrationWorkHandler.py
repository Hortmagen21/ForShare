from response.requestHandler import RequestHandler
from pathlib import Path
import json




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


