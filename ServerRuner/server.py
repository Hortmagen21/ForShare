import os
from http.server import BaseHTTPRequestHandler
from . router import routes
from pathlib import  Path
from  ServerRuner.response.PagesforServerHandler import TemplateHandler
from  ServerRuner.response.BadRequestsHandler import BadRequestHandler
from  ServerRuner.response.StaticHandler import staticHandler

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        #2self.respond()
        split_path=os.path.splitext(self.path)#ми разбиваем путь на все что до формат и сам формат(нам нужен html)подробно в Tester.Ospath
        request_extension=split_path[1]#взяли формат файла
        if request_extension is '' or request_extension is '.html':#проверяем чтоб html
            if self.path in routes:
                handler=TemplateHandler()
                handler.find(routes[self.path])
            else:
                handler = BadRequestHandler()  # ето не html поетому ошибка

        #3else:
            #3handler=BadRequestHandler()#ето не html поетому ошибка
        elif request_extension is '.py':
            handler=BadRequestHandler()
        else:
            handler=staticHandler()
            handler.find(self.path)
        self.respond({
            'handler':handler
        })
    def do_POST(self):
        return

    def handle_http(self,handler):#1(self, status, content_type)#1если просто текст
        #1self.send_response(status)#если код успеха=status продолжем
        #1self.send_header("Content - type", content_type)#устанавливаем headers
        #1self.end_headers()#заканчиваем с headers
        #1route_content=routes[self.path]#проверяет если в пути есть/goodbye то с словаря в router выводит соответсвующий контент
        #1return bytes(route_content, "UTF - 8")#передаем содержимое(что ми виведем) в байтах
        #2status = 200
        #2content_type = "text/plain"
        #2response_content = ""
        #2if self.path in routes:#сверяем что б был такой путь
            #2print(routes[self.path])
            #2route_content=routes[self.path]['PagesforServer']
            #2filepath = Path("PagesforServer/{}".format(route_content))#берем html и format берет нужный route к нужной html
            #2if filepath.is_file():
                #2content_type = "text/html"
                #2response_content = open("PagesforServer/{}".format(route_content))#открываем страницу
                #2response_content = response_content.read()
            #2else:
                #2content_type = "text/plain"
                #2response_content = "404 Not Found"  # если такого нету то ерор
        #2else:
            #2content_type = "text/plain"
            #2response_content = "404 Not Found"#если такого нету то ерор
        #2self.send_response(status)
        #2self.send_header('Content-type', content_type)
        #2self.end_headers()
        #2return bytes(response_content, "UTF-8")
        status_code=handler.getStatus()#берем статус
        self.send_response(status_code)#по аналогие с self.send_response(status)
        if status_code is 200:
            content=handler.getContents()
            self.send_header("Content-type",handler.getContentType())
        else:
            content='404 Not Found'
        self.end_headers()
        if isinstance(content,(bytes,bytearray)):#если уже в байтах(картинки) то не перерабатывать
            return content
        return bytes(content,'UTF-8')

    def respond(self,opts):#opts=handler
        #1content = self.handle_http(200, "text / html")
        #2content = self.handle_http()
        #2self.wfile.write(content)
        response=self.handle_http(opts['handler'])
        self.wfile.write(response)
