import views
import webapp2
from paste import httpserver
import viewsTest

app = webapp2.WSGIApplication([
        ('/',viewsTest.showComics),
        ('/nuevoComic',viewsTest.AddComic),
        ('/editarComic',viewsTest.EditComic),
        ('/eliminarComic',viewsTest.DeleteComic),
        ('/ordenFecha',viewsTest.OrdenFecha),
        ('/buscarNumEntregas', viewsTest.OrdenEntregas),
        ('/buscarFechaMayor', viewsTest.BuscarFechaMayor)
        ],
        debug=True)

def main():
    httpserver.serve(app, host='127.0.0.1', port='8282')
if __name__ == '__main__':
    main()