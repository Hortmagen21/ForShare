from response.requestHandler import RequestHandler
import psycopg2
class FindNameHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"
    def find_name_by_id(self,data):
        database = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM databaseSQL WHERE name LIKE '%{}%'".format(data["fusername"]))
        row=cursor.fetchall()
        isExist=True
        try:
            for i in range(len(row)):#длина 1 части !
                row[i][1]!=""#not end!!
        except IndexError:
            isExist=False
            self.setStatus(404)
        except:
            self.setStatus(404)
        if isExist==True:
            for i in range(len(row)):#длина 1 части !
                if data['my_id']!=str(row[i][0]):#data['my_id] retutn string number
                    data["name"].append(row[i][1]) # массив кортежей(столбцов)
                    data['id'].append(row[i][0])
            self.setStatus(200)

        database.commit()
        cursor.close()
        database.close()
