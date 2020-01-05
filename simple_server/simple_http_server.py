import os
from http import server

class RequestHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self): 
        self.send_response(200, 'ok')
        self.end_headers()
        response = f'hostname: {os.uname()[1]}'
        self.wfile.write(response.encode('utf-8'))
        return

if __name__ == '__main__':
    with server.HTTPServer(('', 8000), RequestHandler) as http_server:
        print('start simple web server...')
        http_server.serve_forever()
