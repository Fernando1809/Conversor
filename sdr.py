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
        
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("PageWeb.html".encode())
    
    def do_POST(self):
        print("Peticion recibida por POST")

        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode()
        data = parse.unquote(data)
        
        matriz = np.fromstring(data, np.float32, sep=',')
        matriz = matriz.reshape(28,28)
        matriz = np.array(matriz)
        matriz = matriz.reshape(1,28,28,1)
        
        prediccion = modelo.predict(matriz,batch_size=1)
        prediccion = str(np.argmax(prediccion))
        print(prediccion)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(prediccion.encode())

print("Server Python :D")
servidor = HTTPServer(("localhost", 3006), servidorBasico)
servidor.serve_forever()