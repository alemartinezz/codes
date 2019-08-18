# Your first Web Server

In this lesson, we are going to write our first web server.

A lot of smartphone apps use HTTP under the hood to send requests and receive data. Web browsers are just the most common — and complicated — user interface for web technology.

But browsers are not the only web client around. HTTP is powerful and widely supported in software, so it's a common choice for programs that need to talk to each other across the network, even if they don't look anything like a web browser.

## Exercise: Running your first web server

So what about the other end, the web server?

Well, it turns out that a web server can actually be a lot simpler than a browser. Browsers have all this user interface and animation and graphics stuff going on. A server just needs to do one thing: handle incoming requests.

### http.server

The Python `http.server` module, can run a built-in web server on your computer. It's not a web app you'd publish to the world; it's a demonstration of Python's HTTP abilities. We'll be referring to this as **the demo server** in this lesson.

**Note**: `http.server` is not recommended for production. It only implements basic security checks.

So, let's get started with the demo web server:

1) Open up a terminal.

2) `cd` into a directory that has some files in it (maybe a directory containing some text files, HTML files, or images ).

3) Run `python3 -m http.server 8000` in your terminal.

When you start up the demo server, it will print a message telling you that it's serving HTTP. Leave it running, and leave the terminal open. Now try accessing http://localhost:8000/ from your browser. You should see something like this, although the file names you see will be different from mine:

And that's the Python demo web server, running on your own computer. It serves up files on your local disk so you can look at them in your browser.

This may not seem like much of a big deal — after all, if you just wanted to access files on your local computer in your browser, you could use `file://` URIs. But the demo server is actually a web server. If you have another computer on the same local network, you could use it to access files served up by this server.

When you put `localhost:8000` in your browser, your browser sends an HTTP request to the Python program you're running. That program responds with a piece of data, which your browser presents to you. In this case, it's showing you a directory listing as a piece of HTML. Use your browser's developer tools to look at the HTML that it sends.

## What's a server anyway?

A server is just a program that accepts connections from other programs on the network.

When you start a server program, it waits for clients to connect to it — like the demo server waiting for your web browser to ask it for a page. Then when a connection comes in, the server runs a piece of code — like calling a function — to handle each incoming connection. A connection in this sense is like a phone call: it's a channel through which the client and server can talk to each other. Web clients send requests over these connections, and servers send responses back.

Take a look in the terminal where you ran the demo server. You'll see a server log with an entry for each request your browser sent:

```python
Serving HTTP on 0.0.0.0 port 8000 ...
127.0.0.1 - - [03/Oct/2016 13:47:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:47:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:48:06] "GET /falafelosofhy.png HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:49:23] code 404, message File not found
127.0.0.1 - - [03/Oct/2016 13:49:23] "GET /NotExistyFile HTTP/1.1" 404 -
```

Hey wow, what is all this stuff? There are some dates and times in there, but what's `GET / HTTP/1.1`, or for that matter `127.0.0.1`? And what's that `200` doing over there?

How do these things relate to the web address you put into your browser? Let's take a look at that next.
