from suds.client import Client
import entrega



class ControllerEntrega(object):
    
    wsdl = 'http://localhost:8080/HumilArt/EntregaWebService?WSDL'
    client = Client(wsdl)
    client.options.cache.clear()
    
    def findEntrega(self, idEnt):
        e = self.client.service.find(idEnt);
        if e:
            en = entrega.Entrega(e['idEntrega'],e['nombre'],e['archivo'],e['fechaCreacion'],e['idComic'])
            return en
        else:
            return None

    def addEntrega(self,nombre,archivo,idComic):
        self.client.service.addEntrega(self,nombre,archivo,idComic)
    def deleteEntrega(self,entrega):
        self.client.service.remove(entrega)
    def editEntrega(self, entrega, nuevoNombre):
        self.client.service.editEntrega(self,entrega,nuevoNombre)
    def findByDate(self):
        self.client.service.findByFechaDescc()
    def findByTamano(self):
        self.client.service.findByTamano();  
    def 