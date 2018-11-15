from suds.client import Client
import comic



class ControllerEntrega(object):
    
    wsdl = 'http://localhost:8080/HumilArt/ComicWebService?WSDL'
    client = Client(wsdl)
    client.options.cache.clear()