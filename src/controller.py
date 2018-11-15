from suds.client import Client
import comic



class Controller(object):
    
    wsdl = 'http://localhost:8080/HumilArt/ComicWebService?WSDL'
    client = Client(wsdl)

    def findComicById(self, idComic):
        c = self.client.service.findComicById(idComic)
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
        self.client.service.editComic(comic,nuevoNombre,nuevaDescripcion)

    def listComics(self):
        listaComics = []
        lista = self.client.service.findAll()
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            listaComics.append(comi)
        return listaComics
        
