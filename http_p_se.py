import http.server

class PersistentRequestHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        super().handle_one_request()
        self.close_connection = False  

handler = PersistentRequestHandler
server_address = ("0.0.0.0", 8000)
httpd = http.server.HTTPServer(server_address, handler)

print("HTTP server serving at port 8000")
httpd.serve_forever()
