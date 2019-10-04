import os

from http.server import BaseHTTPRequestHandler
from router import routes
import cgi
import urllib
from urllib.parse import urlparse
from urllib import parse
import json



from response.PagesforServerHandler import TemplateHandler
from response.BadRequestsHandler import BadRequestHandler
from response.StaticHandler import staticHandler
from response.RegistrationWorkHandler import RegistrationHandler
from response.LoginWorkHandler import LoginHandler
from response.mainInputHandler import InputHandler
from response.FinderById import FindNameHandler
from response.FindGroupHandler import FindGroupHandler
from response.CreatingChat import CreateChatHandler
#urlib
class Server(BaseHTTPRequestHandler):
    def _set_headers(self,handler):
        self.send_response(handler.getStatus())
        self.send_header('Content-type','application/json')
        self.end_headers()
    def message_opener(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        return message

    def do_HEAD(self):
        return
    def do_PUT(self):
        return


    def do_GET(self):
        #2self.respond()
        split_path=os.path.splitext(self.path)#ми разбиваем путь на все что до формат и сам формат(нам нужен html)подробно в Tester.Ospath
        request_extension=split_path[1]#взяли формат файла
        params= os.path.split(split_path[0])#отделяем параметры от ссылки
        parsed_url=parse.urlsplit('/'+self.path)
        print(parsed_url, "parsed_url")
        my_query=urllib.parse.unquote(parsed_url.query)
        print(str(my_query),'my query')
        p='/'+parsed_url[1]+parsed_url[2]
        parameters=dict(parse.parse_qs(parsed_url.query))
        print(parameters,type(parameters),"PARAMSSS")
        if p == '/api/me':
            message =parameters
            handler = InputHandler()
            handler.takeSQLData(message)
            self._set_headers(handler)
            self.wfile.write(bytes(json.dumps(message), 'UTF-8'))
        elif request_extension is '' or request_extension is '.html':#проверяем чтоб html
            if p in routes:
                handler=TemplateHandler()
                handler.find(routes[p])
            else:
                print(self.path,' ',p )
                handler = BadRequestHandler()  # ето не html поетому ошибка

        #3else:
            #3handler=BadRequestHandler()#ето не html поетому ошибка
        elif request_extension is '.py':
            handler=BadRequestHandler()
        else:
            handler=staticHandler()
            handler.find(p)
        self.respond({
            'handler':handler
        })
    def do_POST(self):
        message=self.message_opener()
        if self.path =="/api/login":

            handler=LoginHandler()
            handler.checkSQLData(message)

        elif self.path =="/api/signup":
            handler = RegistrationHandler()
            handler.checkSQLData(message)

        elif self.path =="/api/me":
            handler=InputHandler()
            handler.takeSQLData(message)
        elif self.path == '/api/users/search':
            handler = FindNameHandler()
            handler.find_name_by_id(message)
        elif self.path=="/api/group/search":
            handler=FindGroupHandler()
            handler.find_group(message)
        elif self.path=="/api/chats":
            handler=CreateChatHandler()
            handler.AddChat(message)
        else:
            handler=BadRequestHandler()
        self._set_headers(handler)
        self.wfile.write(bytes(json.dumps(message),'UTF-8'))#json.dumps(message)
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
