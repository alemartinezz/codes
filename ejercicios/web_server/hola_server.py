from http.server import BaseHTTPRequestHandler, HTTPServer


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()


            message = b"<html><body>"
            message += b"<h1>Hello!</h1>"
            message += b"<br>"
            message += b"<h3><a href='/hola'>go to hola</a></h3>"
            message += b"</body></html>"
            self.wfile.write(message)
            print (message)
            return

        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            message = b"<html><body><h1>Hola!</h1>"
            message += b"<br>"
            message += b"<h3><a href='/hello'>back to hello!</a></h3>"
            message += b"</body></html>"
            self.wfile.write(message)
            print (message)
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webServerHandler)
        print ("-- Web Server running on port... %s --" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
