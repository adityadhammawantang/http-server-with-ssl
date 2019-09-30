import http.server
import socketserver
import ssl

port = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("serving at port", port)
    httpd.socket = ssl.wrap_socket(httpd.socket, 
                                   keyfile = "C:\\Users\\Aditya Dhammawan\\Desktop\\privatekey.key", 
                                   certfile = "C:\\Users\\Aditya Dhammawan\\Desktop\\certificate.crt", 
                                   server_side=True)
    httpd.serve_forever()
