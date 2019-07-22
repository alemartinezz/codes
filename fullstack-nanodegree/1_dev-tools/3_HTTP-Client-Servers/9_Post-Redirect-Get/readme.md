# Post-Redirect-Get

There's a very common design pattern for interactive HTTP applications and APIs, called the **PRG** or Post-Redirect-Get pattern. A client `POSTs` to a server to create or update a resource; on success, the server replies not with a `200 OK` but with a `303` redirect. The redirect causes the client to GET the created or updated resource.

This is just one of many, many ways to architect a web application, but it's one that makes good use of HTTP methods to accomplish specific goals. For instance, wiki sites such as Wikipedia often use Post-Redirect-Get when you edit a page.

For the **messageboard** server, Post-Redirect-Get means:

1. You go to http://localhost:8000/ in your browser. Your browser sends a GET request to the server, which replies with a `200 OK` and a piece of HTML. You see a form for posting comments, and a list of the existing comments. (But at the beginning, there are no comments posted yet.)
2. You write a comment in the form and submit it. Your browser sends it via `POST` to the server.
3. The server updates the list of comments, adding your comment to the list. Then it replies with a `303` redirect, setting the `Location: /` header to tell the browser to request the main page via `GET`.
4. The redirect response causes your browser to go back to the same page you started with, sending a `GET` request, which replies with a `200 OK` and a piece of HTML…

One big advantage of Post-Redirect-Get is that as a user, every page you actually see is the result of a `GET` request, which means you can bookmark it, reload it, and so forth — without ever accidentally resubmitting a form.

## Exercise: Messageboard, Part Three

Update the **messageboard** server to a full Post-Redirect-Get pattern, as described above. You'll need both `do_GET` and `do_POST` handlers; the `do_POST` handler should reply with a 303 redirect with no response body.

The starter code for this exercise is in the `5_MessageboardPartThree` directory. I've added the logic that actually stores the messages into a list; all you need to do is implement the HTTP steps described above.

When you're done, test it in your browser and with the `test.py` script, as before.

Check off these steps as you complete them in the Messageboard Part Three exercise.
- In the `do_POST` method, send a 303 redirect back to the root page.
- In the `do_GET` method, assemble the response data together out of the form template and the stored messages.
- Run the server and test it in your browser.
- Run the tests in `test.py` with the server running. 


## HTTP Server

0. Create server file

```python
vim HelloServer.py
```

1. Import `HTTPServer`, `BaseHTTPRequestHandler`, `parse_qs`

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
```

```python
from urllib.parse import parse_qs
```

2. Create the GET response HTML body

```python
form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''
```

3. Create an array for storing the user's input

```python
memory = []
```

3. Create an instance of _**http.server.BaseHTTPRequestHandler**_. Inside you will define GET y POST responses.

```python
class handler(BaseHTTPRequestHandler):

    # Definir método para requests GET
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Response body
        self.wfile.write("Hello, HTTP!\n".encode())

    # Definir método para requests POST
    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the message
        data = self.rfile.read(length).decode()
        message = parse_qs(data)["message"][0]

        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store it in memory.
        memory.append(message)

        # Send a 303 back to the root page
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
```

7. Ejecutar

```python
python3 HelloServer.py
```

8. Test

```python
python3 HelloServer.py
```

### Todo junto

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

memory = []

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the message
        data = self.rfile.read(length).decode()
        message = parse_qs(data)["message"][0]

        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store it in memory.
        memory.append(message)

        # Send a 303 back to the root page
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with the messages in it.
        mesg = form.format("\n".join(memory))
        self.wfile.write(mesg.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
```