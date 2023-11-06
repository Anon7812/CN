import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

server_address = ("0.0.0.0", 8000)

httpd = socketserver.TCPServer(server_address, handler)

print("HTTP server serving at port 8000")
httpd.serve_forever()