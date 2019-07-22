## Http GET Request

Take a look back at the server logs on your terminal, where the demo server is running. When you request a page from the demo server, an entry appears in the logs with a message like this:

```
127.0.0.1 - - [03/Oct/2016 15:45:50] "GET /readme.png HTTP/1.1" 200 -
```

Take a look at the part right after the date and time. Here, it says `"GET /readme.png HTTP/1.1"`. This is the text of the **request line** that the browser sent to the server. This log entry is the server telling you that it received a request that said, literally, `GET /readme.png HTTP/1.1`.

### This request has three parts.

1. The word `GET` is the **method** or **HTTP verb** being used; this says what kind of request is being made. GET is the verb that clients use when they want a server to send a resource, such as a web page or image. Later, we'll see other verbs that are used when a client wants to do other things, such as submit a form or make changes to a resource.

2. `/readme.png` is the **path** of the resource being requested. Notice that the client does not send the whole URI of the resource here. It doesn't say https://localhost:8000/readme.png. It just sends the path.

3. Finally, `HTTP/1.1` is the **protocol** of the request. Over the years, there have been several changes to the way HTTP works. Clients have to tell servers which dialect of HTTP they're speaking. HTTP/1.1 is the most common version today.

### Exercise: Send a request manually

You can use `ncat` to connect to the demo server and send it an HTTP request by hand. (Make sure the demo server is still running!)

Use `ncat 127.0.0.1 8000` to connect your terminal to the demo server.

Then type these two lines:
```
GET / HTTP/1.1
Host: localhost
```

After the second line, **press Enter twice**. As soon as you do, the response from the server will be displayed on your terminal. Depending on the size of your terminal, and the number of files the web server sees, you will probably need to **scroll up** to see the beginning of the response!
