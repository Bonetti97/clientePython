import views
import webapp2
from paste import httpserver
import viewsEntrega

app = webapp2.WSGIApplication([
        ('/',views.showComics), 
        ('/newComic',views.AddComic), 
        ('/editarComic/([\d]+)', views.EditComic),
        ('/delete/([\d]+)', views.DeleteComic),
        ('/ordenAlfabetico',views.OrdenAlfabetico),
        ('/ordenFecha',views.OrdenFecha),
        ('/buscarNombre', views.BuscarNombre),
        ('/buscarFechaMayor', views.BuscarFechaMayor),
        ('/buscarNumEntregas', views.OrdenEntregas),
        ('/entregasComic/([\d]+)',viewsEntrega.showEntregasComic),
        ('/newEntrega/([\d]+)',viewsEntrega.AddEntrega)
        ],
        debug=True)

def main():
    httpserver.serve(app, host='127.0.0.1', port='8181')
if __name__ == '__main__':
    main()