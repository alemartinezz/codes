# !usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer


# Use to decipher message sent from the server
import cgi


# Import everything
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant_setup import Base, Restaurant, MenuItem


# Create session and connect
engine = create_engine("postgres://vagrant:laCumbre1@/restaurant")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        """
            Do_get method for handling GET request.
        """
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = b"<html><body><h1>Restaurants..!</h1> </br>"
                output += b"<h4><a href='/restaurant/new'>Crear nuevo Restaurant...</a></h4> <br><br>"
                for restaurant in restaurants:
                    output += restaurant.name.encode('ascii')
                    output += b"<br>"
                    output += b"<a href='/restaurants/%s/edit'>Editar</a> - " % str(restaurant.id).encode('ascii')
                    output += b"<a href='/restaurants/%s/delete'>Borrar</a>" % str(restaurant.id).encode('ascii')
                    output += b"<br><br>"
                output += b"</body></html>"

                self.wfile.write(output)
                return


            elif self.path.endswith("/restaurant/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = b"<html><body>"
                output += b"<h3><a href='/restaurants'>Inicio</a></h3> <br>"
                output += b"<h2>Crear nuevo Restaurant</h2>"
                output += b"<form method='POST' enctype='multipart/form-data' action='/restaurant/new'>"
                output += b"<input name='newRestaurantName' type='text' placeholder='name it' > "
                output += b"<input type='submit' value='Create'>"
                output += b"</form></html></body>"

                self.wfile.write(output)
                return


            elif self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('content-type', 'text/html')
                    self.end_headers()

                    message = b"<html><body>"
                    message += b"<h1>%s</h1>" % myRestaurantQuery.name.encode('ascii')
                    message += b"<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath.encode('ascii')
                    message += b"<input name='NewRestaurant' type='text' placeholder='new name'>"
                    message += b"<input type='submit' value='Update'>"
                    message += b"</form></body></html>"

                    self.wfile.write(message)
                    return


            elif self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = b"<html><body>"
                    output += b"<h1>Esta seguro que desea eliminar: %s?" % myRestaurantQuery.name.encode('ascii')
                    output += b"<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath.encode('ascii')
                    output += b"<input type='submit' value='Delete'>"
                    output += b"</form></body></html>"

                    self.wfile.write(output)
                    return


        except:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        """
            Do_get method for handling GET request.
        """
        try:

            if self.path.endswith("/restaurant/new"):
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "ascii")

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name = messagecontent[0].decode("ascii"))
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            
            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "ascii")

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('NewRestaurant')

                    restaurantIDPath = self.path.split('/')[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                    if myRestaurantQuery:
                        myRestaurantQuery.name = messagecontent[0].decode('ascii')
                        session.add(myRestaurantQuery)
                        session.commit()

                        # redirect to resturants page
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()


            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                if myRestaurantQuery:
                    session.delete(myRestaurantQuery)
                    session.commit()
                    
                    # redirect to resturants page
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass


def main():
    """
        Main function for running the Web server handler class.
    """
    try:
        port = 8000
        server = HTTPServer(('', port), webServerHandler)
        print ("-- Web Server running on port... %s --" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print (" entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    """
        Execute the main function.
    """
    main()
