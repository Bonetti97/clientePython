from suds.client import Client
import views

client = Client('http://localhost:8080/HumilArt/ComicWebService?WSDL')
#print client.service.findAll()
#print client.service.count()
client.service.addComic("prueba","hu")


#print client
