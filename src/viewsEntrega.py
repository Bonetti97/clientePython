import os
import webapp2
import jinja2
from controllerEntrega import ControllerEntrega
from controller import Controller
import cgi

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))



class BaseHandler(webapp2.RequestHandler):

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))
   
   
class showEntregasComic(BaseHandler):
    def get(self,comicID):     
        ent = Controller().getEntregasComic(comicID)
        self.render_template('entregasComic.html', {'listaEntregas': ent,'comicID': comicID}) 
            
class AddEntrega(BaseHandler):
    def get(self,comicID):
        self.render_template('newEntrega.html', {'comicID':comicID})
    
    def post(self,comicID):
        ControllerEntrega().addEntrega(self.request.get('nombreEntrega'),"hola",comicID)
        #archivo = self.request.POST.get("archivoEntrega",None);
        #if isinstance(archivo, cgi.FieldStorage):
         #   file_name = archivo.filename
          #  file_data = archivo.file.read
            
        # he estado probando muchas cosas, buscando sobre cual es el tipo del archivo que cogemos.
        #He encontrado que es FieldStorage pero no consigo pasarlo para que java lo lea.
        #ave si lo conseguis.
        
        #ControllerEntrega().addEntrega(self.request.get('nombreEntrega'),,comicID)
        return webapp2.redirect('/entregasComic/'+comicID);     
    
        
class EditEntrega(BaseHandler):
    def get(self, entregaID):      
        en = ControllerEntrega().findEntrega(entregaID)
        self.render_template('editarEntrega.html', {'entrega': en})
        
    def post(self,entregaID):
        nombre = self.request.get('nombreEntrega')
        entregaAux=ControllerEntrega().findEntrega(entregaID)
        ControllerEntrega().editComic(entregaID, nombre);
        return webapp2.redirect('/entregasComic/'+str(entregaAux.idComic.idComic))
    
class DeleteEntrega(BaseHandler):
    def get(self, entregaID):
        entregaAux=ControllerEntrega().findEntrega(entregaID)
        ControllerEntrega().deleteEntrega(entregaID)
        return webapp2.redirect('/entregasComic/'+str(entregaAux.idComic.idComic))
    
class OrdenaFechaDesc(BaseHandler):
    def get(self, comic):
        lista=ControllerEntrega().findByDate(comic)
        self.render_template('entregasComic.html', {'listaEntregas':lista})

class OrdenNombreInverso(BaseHandler):
    def get(self, comic):
        lista=ControllerEntrega().listEntregasNombreInverso(comic)
        self.render_template('entregasComic.html', {'listaEntregas':lista})

class BuscarFechaMayorEntrega(BaseHandler):
    def get(self,comic):
        fecha=self.request.get('busquedaFechaMayorEntrega')
        lista=ControllerEntrega().filtrarPorFecha(fecha,comic)
        self.render_template('entregasComic.html', {'listaEntregas':lista})
        