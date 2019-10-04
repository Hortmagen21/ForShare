from response.requestHandler import RequestHandler
import psycopg2
from pathlib import Path
import json

import config


class InputHandler(RequestHandler):
    def __init__(self):  # создали конструктор
        super().__init__()  # err in ajax
        self.contentType = "application/json"

    def takeSQLData(self, data):
        self.setStatus(200)
        database = psycopg2.connect(config.DATABASE_URL)
        cursor = database.cursor()
        cursor.execute("SELECT * FROM databaseSQL WHERE id='{}'".format(int(data["id"][0])))
        #data["getname"]["name"]=cursor.fetchall()[0][1]
        data['name'][0]=cursor.fetchall()[0][1]
        self.contents=data['name'][0]
        database.commit()
        cursor.close()
        database.close()

    def findUserById(self, user_id):
        conn = psycopg2.connect(config.DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM databaseSQL WHERE id=%s", (user_id,))

        id, username, _ = cursor.fetchone()

        user = {
            "id": id,
            "username": username
        }
        cursor.close()
        conn.close()

        return user

    def loginUser(self, username, password):
        conn = psycopg2.connect(config.DATABASE_URL)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM databaseSQL WHERE name=%s", (username,))

        user_if_exists = cursor.fetchone()

        cursor.close()
        conn.close()

        if user_if_exists == None:
            return None
        else:
            return {
                "id": user_if_exists[0],
                "username": user_if_exists[1],
            }
