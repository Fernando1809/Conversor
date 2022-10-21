import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
from http.server import BaseHTTPRequestHandler, HTTPServer
 
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion recibida por GET")
        if self.path == '/':
            self.path = '/PageWeb.html'
        try:
            #Reading the file
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        self.end_headers()
    
    def do_POST(self):
     if self.path == '/PageWeb.html':
         SimpleJSONRPCRequestHandler.do_POST(self)
     else:
         __pychecker__ = 'no-classattr'
         SimpleHTTPRequestHandler.do_POST(self)

print("Server Python :D")
servidor = HTTPServer(("localhost", 3006), servidorBasico)
servidor.serve_forever()