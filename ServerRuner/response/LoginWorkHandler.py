from response.requestHandler import RequestHandler
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
            if a["data"][i]["username"]==data["username"] and a["data"][i]["password"]==data["password"]:
                self.setStatus(200)
                isDuplicate = True
            i = i + 1
        if isDuplicate==False:
            self.setStatus(404)
