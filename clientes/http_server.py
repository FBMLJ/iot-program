import http.server
import socketserver
from http.server import BaseHTTPRequestHandler
PORT = 8000

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print(self.request)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(bytes(message, "utf8"))

 
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()