from response.requestHandler import RequestHandler
import psycopg2
class CreateChatHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"
    def AddChat(self,data):
        #if constraction dublicate
        database = psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
        cursor = database.cursor()
        cursor.execute("INSERT INTO chat (chat_name,members_count) VALUES ('{}',2)".format(data["name_receiver"]))
        cursor.execute("SELECT max(chat_id) from chat")
        row = cursor.fetchall()
        chat_id=row[0][0]
        cursor.execute("INSERT INTO chat_members (chat_id,user_id) VALUES ('{id_chat}','{id_receiver}')".format(id_chat=chat_id,id_receiver=data["my_Id"]))
        cursor.execute("INSERT INTO chat_members (chat_id,user_id) VALUES ('{id_chat}','{id_receiver}')".format(id_chat=chat_id,id_receiver=data["int_receiver"]))
        self.setStatus(200)
        database.commit()
        cursor.close()
        database.close()
