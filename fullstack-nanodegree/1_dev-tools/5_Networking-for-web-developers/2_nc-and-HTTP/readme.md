### How to listen on port 3456 with netcat?

```unix
nc -l 3456
```

```unix
nc localhost 3456
```


## Experiment with nc and HTTP

To get a better understanding of what netcat can do here, take another look at the nc manual page. Specifically, there's a section in there titled "Talking to Servers". Take a look at that section. Then, using what you learn there and what you've seen already in this lesson, try some experiments of your own with nc and web servers.

Here are some ideas:

### Sending HTTP headers

When you send an HTTP request using nc, the headers occur on lines after the HTTP verb itself. The Host: header you've seen in the previous exercises is required by the HTTP 1.1 protocol. What happens if you make requests that don't provide this header?

Are there other headers that it might be interesting to try sending? You can find a list of HTTP headers at Wikipedia.

What happens if you send a header you just made up?

What happens if you send an HTTP verb you just made up, instead of GET or HEAD or POST or the other real ones?
Interpreting responses

If you send a well-formed request for host www.udacity.com to the Udacity web server, you may get back a 302 Found response with a Location: header. What does this header mean? What would a browser do in response to receiving that header?
Fetching content

Most of the requests you have sent using nc are HEAD requests. HEAD is an HTTP verb that asks the server to send just the headers for a resource, rather than sending the full data. You can do GET requests as well, though:

```python
printf "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n" | nc www.example.com 80
```

How would you separate the headers from the data in the response you get here?

If you would like to save the results of an nc command to a file, you can do this with the > shell redirection operator. For instance, this will save the results to the file example.txt:

```python
printf "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n" | nc www.example.com 80 > example.txt
```
