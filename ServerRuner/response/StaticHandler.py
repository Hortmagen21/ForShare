from response.requestHandler import RequestHandler
import os
class staticHandler(RequestHandler):
    def __init__(self):
        self.filetypes={
            '.js':'text/javascript',
            '.css':'text/css',
            '.jpg':'image/jpg',
            '.png':'image/png',
            'not found':'text/plain'
        }
    def find(self,file_path):
        split_path=os.path.splitext(file_path)
        extension=split_path[1]#узнаем формат
        try:
            print(extension,'тип файла')
            if extension in ('.jpg','.jpeg','.png'):
                self.contents=open('response/public{}'.format(file_path), 'rb')
            else:
                print('public{}'.format(file_path),'путь к файлу')
                self.contents=open('response/public{}'.format(file_path),'r')
            self.setContentType(extension)
            self.setStatus(200)
            return True
        except:
            self.setContentType('not found')
            self.setStatus(404)
            return False
    def setContentType(self,ext):
        self.contentType=self.filetypes[ext]