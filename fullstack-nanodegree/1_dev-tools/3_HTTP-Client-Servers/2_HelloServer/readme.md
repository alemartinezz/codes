# http.server - Python's module

**http.server** module defines classes for implementing HTTP servers (Web servers).

**Note**: http.server is not recommended for production. It only implements basic security checks. But it is a first step to understand the lower level behavior of a Web server.

These modules are written in object-oriented Python. You should already be familiar with creating class instances, defining subclasses, and defining methods on classes.

## Servers and handlers

Web servers using http.server are made of two parts: the **_HTTPServer class_**, and a **_request handler_ class**. The HTTPServer class, is built into the module and is the same for every web service.
It knows how to listen on a port and accept HTTP requests from clients. Whenever it receives a request, it hands that request off to the second part — a request handler — which is different for every web service.

Here's what your Python code will need to do in order to run a web service:

0. Create Server file

```python
vim HelloServer.py
```

1. Import `http.server` and `BaseHTTPRequestHandler`or at least the pieces of it that you need.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
```

2. Create an instance of **http.server.BaseHTTPRequestHandler** This is your handler class.

```python
class HelloHandler(BaseHTTPRequestHandler):
```

3. Define a method on the handler class for each HTTP verb you want to handle. (The only HTTP verb you've seen yet in this course is GET, but that will be changing soon.) The method for **GET requests** has to be called **do_GET**. Inside the method, call built-in methods of the handler class to read the HTTP request and write the response.

```python
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())
```

5. Create an instance of http.server.HTTPServer, giving it your handler class and server information — particularly, the port number.

```python
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
```

6. Call the HTTPServer instance's serve_forever method. Once you call the HTTPServer instance's **serve_forever** method, the server does that — it runs forever until stopped.

```python
httpd.serve_forever()
```

7. Execute

```python
python3 HelloServer.py
```

8. Test

```python
python3 HelloServer.py
```

Just as in the last lesson, if you have a Python server running and you want to stop it, type Ctrl-C into the terminal where it's running. (You may need to type it two or three times.)
For more information, you can check Python Documentation.

## Todo junto

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
```


## Let's take a look at each part of this code, line by line.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
```

The http.server module has a lot of parts in it. For now, this program only needs these two. I'm using the **from** syntax of **import** so that I don't have to type **http.server** over and over in my code.

```python
class HelloHandler(BaseHTTPRequestHandler):
def do_GET(self):
```

This is the handler class. It inherits from the **BaseHTTPRequestHandler** parent class, which is defined in **http.server**. I've defined one method, **do_GET**, which handles HTTP GET requests. When the web server receives a GET request, it will call this method to respond to it.

As you saw in the previous lesson, there are three things the server needs to send in an HTTP response: a status code, some headers, and the response body. The handler parent class has methods for doing each of these things. Inside **do_GET**, I just call them in order.

```python
# First, send a 200 OK response.
self.send_response(200)
```

The first thing the server needs to do is send a 200 OK status code; and the **send_response** method does this. I don't have to tell it that 200 means OK; the parent class already knows that.

```python
# Then send headers.
self.send_header('Content-type', 'text/plain; charset=utf-8')
self.end_headers()
```

The next thing the server needs to do is send HTTP headers. The parent class supplies the **send_header** and **end_headers** methods for doing this. For now, I'm just having the server send a single header line — the Content-type header telling the client that the response body will be in UTF-8 plain text.

```python
# Now, write the response body.
self.wfile.write("Hello, HTTP!\n".encode())
```

The last part of the **do_GET** method writes the response body.

The parent class gives us a variable called **self.wfile**, which is used to send the response. The name wfile stands for writeable file. Python, like many other programming languages, makes an analogy between network connections and open files: they're things you can read and write data to. Some file objects are read-only; some are write-only; and some are read/write.

**self.wfile** represents the connection from the server to the client; and it is write-only; hence the name. Any binary data written to it with its **write** method gets sent to the client as part of the response. Here, I'm writing a friendly hello message.

What's going on with **.encode()** though? We'll get to that in a moment. Let's look at the rest of the code first.

```python
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
```

This code will run when we run this module as a Python program, rather than importing it. The **HTTPServer** constructor needs to know what address and port to listen on; it takes these as a tuple that I'm calling **server_address**. I also give it the **HelloHandler** class, which it will use to handle each incoming client request.

At the very end of the file, I call **serve_forever** on the **HTTPServer**, telling it to start handling HTTP requests. And that starts the web server running.
