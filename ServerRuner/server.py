import os

from http.server import BaseHTTPRequestHandler
from router import routes
import cgi

import json


from response.PagesforServerHandler import TemplateHandler
from response.BadRequestsHandler import BadRequestHandler
from response.StaticHandler import staticHandler
from response.RegistrationWorkHandler import RegistrationHandler
from response.LoginWorkHandler import LoginHandler

class Server(BaseHTTPRequestHandler):
    def _set_headers(self,handler):
        self.send_response(handler.getStatus())
        self.send_header('Content-type','application/json')
        self.end_headers()
    def do_HEAD(self):
        return
    def do_PUT(self):
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
        ctype,pdict=cgi.parse_header(self.headers.get('content-type'))
        if ctype!= 'application/json':
            self.send_response(400)
            self.end_headers()
            return
        print(ctype)
        length=int(self.headers.get('content-length'))
        print(length)
        message=json.loads(self.rfile.read(length))
        if self.path == "/login":
            handler=LoginHandler()
            handler.check(message)
        else:
            handler = RegistrationHandler()
            #handler.checkandadd(message)
            handler.checkSQLData(message)#принимает только инт пароль
        self._set_headers(handler)
        self.wfile.write(bytes(json.dumps(message),'UTF-8'))
        #if self.path=="/"
        #content_len=int(self.headers.get('Content-Length'))
        #post_body =self.rfile.read(content_len)




    def handle_http(self,handler):
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

    def respond(self,opts):
        response=self.handle_http(opts['handler'])
        self.wfile.write(response)
