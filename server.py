

from http.server import BaseHTTPRequestHandler, HTTPServer
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5)+1):
       if n % x == 0:
           return False
    return True

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if is_prime(5):
                self.wfile.write(b'<h1>liczba jest pierwsza<h1><h1> Dzien bez mema to dzien stracony </h1><img src="https://puzzlemania-154aa.kxcdn.com/products/2024/puzzle-schmidt-1000-pieces-random-galaxy.webp" alt="Kot w garniturze"><p>Kiedy probujesz wygladac profesjonalnie, ale jestes tylko kotem.</p>')
            else:
                self.wfile.write(b'liczba nie jest pierwsza')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

host = 'localhost'
port = 8000

with HTTPServer((host, port), MyHandler) as server:
    print(f'Server running at http://{host}:{port}')
    server.serve_forever()







