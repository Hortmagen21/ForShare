from  response.requestHandler import RequestHandler
class BadRequestHandler(RequestHandler):#если что то пошло не так то вызиваем етот класс
    def __init__(self):
        super().__init__()
        self.contentType="text/plain"
        self.setStatus(404)