# A server for POST
In the next few exercises, you'll be building a **messageboard server**.

When a user goes to the main page in their browser, it'll display a form for writing messages, as well as a list of the previously written messages.

Submitting the form will send a request to the server, which stores the submitted message and then re-displays the main page.

In order to test your **messageboard server**, you'll need to install the requests module, which is a Python module for making HTTP requests.

We'll see much more about this module later in this lesson. For now, just run `pip3 install requests` in your terminal to install it.

### Question 1 of 3
Which HTTP methods do you think this server will need to use?
- Only GET
- Only POST
- GET for submitting messages, POST for viewing them.
- GET for viewing messages, and POST for submitting them.


## Why don't we want to use GET for submitting the form?

Imagine if a user did this. They write a message and press the submit button … and the message text shows up in their URL bar. If they press reload, it sends the message again. If they bookmark that URL and go back to it, it sends the message again.

This doesn't seem like such a great experience. So we'll use POST for message submission, and GET to display the main page.


## POST handlers read the request body

Previously in the **HelloServer** exercise, you've written handler classes that have just a single method, `do_GET`.

But a handler class can have `do_POST` as well, to support GET and POST requests. This is exactly how the **messageboard server** will work.

When a GET request comes in, the server will send the HTML form and current messages. When a POST request comes in with a new message, the server will store the message in a list, and then return all the messages it's seen so far.

The code for a `do_POST` method will need to do some pretty different things from a `do_GET` method. When we're handling a GET request, all the user data in the request is in the URI path. But in a POST request, it's in the request body.

Inside `do_POST`, our code can read the request body by calling the `self.rfile.read` method. `self.rfile` is a file object, like the `self.wfile` we saw earlier — but `rfile` is for reading the request, rather than writing the response.

However, `self.rfile.read` needs to be told how many bytes to read … in other words, how long the request body is.

How do you think our code can tell how much data is in the request body of a POST request from a web browser?

### Question 2 of 3
How do you think our code can tell how much data is in the request body of a POST request from a web browser?
- The browser always send exactly 1024 bytes.
- Our code should read repeatedly until it gets an empty string.
- The browser sends the lenght of the request body in the `content-lenght` header.
- The first two bytes of the request body encode the lenght of the request body.


## Headers are strings (or missing)
The handler class gives us access to the HTTP headers as the instance variable `self.headers`, which is an object that acts a lot like a Python dictionary. The keys of this dictionary are the header names, but they're case-insensitive: it doesn't matter if you look up `'content-length'` or `'Content-Length'`. The values in this dictionary are strings: if the request body is 140 bytes long, the value of the `Content-length` entry will be the string `"140"`. We need to call `self.rfile.read(140)` to read 140 bytes; so once we read the header, we'll need to convert it to an integer.

But in an HTTP request, it's also possible that the body will be empty, in which case the browser might not send a `Content-length` header at all. This means we have to be a little careful when accessing the headers from the self.headers object. If we do `self.headers['content-length']` and there's no such header, our code will crash with a `KeyError`. Instead, we'll use the `.get` dictionary method to get the header value safely.

So here's a little bit of code that can go in the `do_POST` handler to find the length of the request body and read it:
```
length = int(self.headers.get('Content-length', 0))
data = self.rfile.read(length).decode()
```

Once you read the message body, you can use `urllib.parse.parse_qs` to extract the POST parameters from it.

With that, you can now build a `do_POST` method!


## Exercise

### Messageboard, part one
The first step to building the **messageboard** server is to build a server that accepts a POST request and just echoes it back to the browser. The starter code for this exercise is in `Lesson-2/3_MessageboardPartOne`.

There are several steps involved in doing this, so here's a checklist
- Find the lenght of the POST request data.
- Read the correct amount of request data.
- Extract the "message" field from the request data.
- Run the `MessageboardPartOne.py` server.
- Open the `MessageboardPartOne.html` in browser and submit it.
- Run the test script `test.py` with the server running.


### Messageboard, Part Two
So far, this server only handles POST requests. To submit the form to it, you have to load up the form in your browser as a separate HTML file. It would be much more useful if the server could serve the form itself.

This is pretty straightforward to do. You can add the form in a variable as a Python string (in triple quotes), and then write a `do_GET` method that sends the form.

You can choose to start from where you left off in the previous exercise; or if you like, you can start from the code in the `4_MessageboardPartTwo` directory.

When you're done, you should have a server that you can access in your browser at http://localhost:8000/. Going there should display the form. Submitting the form should get the message echoed back. That's most of the way to a **messageboard server** ... let's keep going!


- Add a string variable that contains the HTML form from `Messageboard.html`
- Add a `do_GET` method that returns the form.
- Run the server and test it in your browser at http://locahost:8000.
- Run the tests in `test.py` with the server running.


## Question 3
Bring your messageboard server up and send it some requests from your browser with different URI paths, like http://localhost:8000/bears or http://localhost:8000/udacity-rocks/my-foxes. Does it do anything different based on the URI path?

- Yes, it does.
- No, it doesn`t.


## Todo junto

1. Crear archivo del servidor HTTP
```
vim messageboard_server.py
```
```python
#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)
        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # Then encode and send response body (the form).
        self.wfile.write(form.encode())

    def do_POST(self):
        # 1. How long was the message?
        length = int(self.headers.get('Content-length', 0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # 3. Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
```

2. Ejecutarlo
```
python3 messageboard_server.py
```

3. Crear archivo de test
```
vim test.py
```
```python
import requests, random, socket

def test_connect():
    '''Try connecting to the server.'''
    print("Testing connecting to the server.")
    try:
        with socket.socket() as s:
           s.connect(("localhost", 8000))
        print("Connection attempt succeeded.")
        return None
    except socket.error:
        return "Server didn't answer on localhost port 8000.  Is it running?"

def test_POST():
    '''The server should accept a POST and return the "message" field.'''
    print("Testing POST request.")
    mesg = random.choice(["Hi there!", "Hello!", "Greetings!"])
    uri = "http://localhost:8000/"
    try:
        r = requests.post(uri, data = {'message': mesg})
    except requests.RequestException as e:
        return ("Couldn't communicate with the server. ({})\n"
                "If it's running, take a look at its output.").format(e)
    if r.status_code == 501:
        return ("The server returned status code 501 Not Implemented.\n"
                "This means it doesn't know how to handle a POST request.\n"
                "(Is the correct server code running?)")
    elif r.status_code != 200:
        return ("The server returned status code {} instead of a 200 OK."
                ).format(r.status_code)
    elif r.text != mesg:
        return ("The server sent a 200 OK response, but the content differed.\n"
                "I expected '{}' but it sent '{}'.").format(mesg, r.text)
    else:
        print("POST request succeeded.")
        return None


if __name__ == '__main__':
    tests = [test_connect, test_POST]
    for test in tests:
        problem = test()
        if problem is not None:
            print(problem)
            break
    if not problem:
        print("All tests succeeded!")
```

4. Ejecutarlo
```
python3 test.py
```