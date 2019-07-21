class MockFile():#если ми не сможем прочитать файл обычним read() то видаст False
    def read(self):
        return False
class RequestHandler():
    def __init__(self):#создали конструктор
        self.contentType=""#создавая обьект у нас есть 2 параметра contentType,contents
        self.contents=MockFile()
    def getContents(self):#если нужно взять contents
        return self.contents.read()
    def read(self):#просмотр файла врод
        return self.contents
    def setStatus(self,status):#код успеха поставить
        self.status=status
    def getStatus(self):#взять
        return self.status
    def getContentType(self):#взять тип контента
        return self.contentType
    def getType(self):
        return "static"