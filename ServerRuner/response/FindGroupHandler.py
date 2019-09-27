from response.requestHandler import RequestHandler
import psycopg2
class FindGroupHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"
    def find_group(self,data):
        database = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM chat WHERE chat_name LIKE '%{}%'".format(data["group_name"]))
        row = cursor.fetchall()
        isExist = True
        try:
            for i in range(len(row)):  # длина 1 части !
                row[i][1] != ""  # not end!!
        except IndexError:
            isExist = False
            self.setStatus(404)
        if isExist == True :
            for i in range(len(row)):  # длина 1 части !
                # row[i][1]!=""#not end!!
                if(row[i][2]>2):
                    data["group_names"].append(row[i][1])  # массив кортежей(столбцов)
                    data['group_ids'].append(row[i][0])
            self.setStatus(200)
        database.commit()
        cursor.close()
        database.close()