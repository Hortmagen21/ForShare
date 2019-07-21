import time
from http.server import HTTPServer
from ServerRuner.server import Server
HOST_NAME='localhost'
PORT_NUMBER=8080
#if __name__ == '__main__':#убеждаемся что ето именно файл main
httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)#оздаем обьект сервера
print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))
    #master branche
