import os
import webapp2
import jinja2
from controller import Controller



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
        
        
class showComics(BaseHandler):
    def get(self):     
        cos = Controller().listComics()   
        self.render_template('comics.html', {'listaComic': cos})
        
class AddComic(BaseHandler):
    def get(self):
        self.render_template('newComic.html', {})
    
    def post(self):
        print self.request.get('nombreComic')
        Controller().addComic(self.request.get('nombreComic'), 
                              self.request.get('descripcionComic'))
        return webapp2.redirect('/')
        
class EditComic(BaseHandler):
    def get(self, comicID):      
        co = Controller().findComicById(int(comicID))
        self.render_template('editarComic.html', {'comic': co})
        
    def post(self,comicID):
        nombre = self.request.get('nombreComic')
        descripcion = self.request.get('descripcionComic')
        Controller().editComic(comicID, nombre, descripcion)
        return webapp2.redirect('/')

class DeleteComic(BaseHandler):
    def get(self, comicID):
        co = Controller().findComicById(int(comicID))
        print co.nombre
        print co.descripcion
        print co.idComic
        Controller().deleteComic(co)
        return webapp2.redirect('/')
        
        
        
        
        
        
        
        
        
        
        
        