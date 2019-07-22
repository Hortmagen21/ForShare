from response.requestHandler import RequestHandler
class TemplateHandler(RequestHandler):
    def __init__(self):#создали конструктор
        super().__init__()#взяли все с конструктора у RequestHandler(пример super в Tester.Superr)
        self.contentType='text/html'
    def find(self,routeDate):#функция чтоб найти по route файл
        try:
            template_file=open('PagesforServer/{}'.format(routeDate["PagesforServer"]))#проверяем открываеться ли по данной сылке файл
            self.contents=template_file#если да то помещяем в ранее созданный contents в конструкторе RequestHandler от которого ми наследуемся
            self.setStatus(200)#
            return True
        except:
            self.setStatus(404)
            return False