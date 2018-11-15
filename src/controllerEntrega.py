from suds.client import Client
import comic



class ControllerEntrega(object):
    
    wsdl = 'http://localhost:8080/HumilArt/EntregaWebService?WSDL'
    client = Client(wsdl)
    client.options.cache.clear()
    
    def findEntregaById(self, idComic):
        c = self.client.service.findEntregaById();
        if c:
            cam = comic.Comic(c['idComic'],c['nombre'],c['descripcion'],c['fechaCreacion'])
            return cam
        else:
            return None

    def addComic(self,nombre,descripcion):
        self.client.service.addComic(nombre,descripcion)
    def deleteComic(self,comic):
        self.client.service.remove(comic)
    def editComic(self, comic, nuevoNombre,nuevaDescripcion):