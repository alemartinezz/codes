# Making requests

The `requests` library is a Python library for sending requests to web servers and interpreting the responses. It's not included in the Python standard library, though; you'll need to install it. In your terminal, run `pip3 install requests` to fetch and install the `requests` library.

Then take a look at the quickstart documentation for `requests` and try it out.

### Question 1 of 3
Assuming you've still got your messageboard server running on port 8000, how would you send a GET request to it using the `requests` library? Which of these options works?

- `requests.fetch("http://localhost/"port=8000)`
- `requests.fetch("http://localhost:8000/")`
- `requests.transmit("GET","http://localhost:8000", "/")`

## Response objects
When you send a request, you get back a `Response` object. Try it in your Python interpreter:
```python
>>> import requests
>>> a = requests.get('http://www.udacity.com')
>>> a
<Response [200]>
>>> type(a)
<class 'requests.models.Response'>
```

### Question 2 of 3
Use the documentation for the `requests` module to answer this question!

If you have a response object called `r`, how can you get the response body — for instance, the HTML that the server sent?
 - `r.text`
 - `r.content`
 - Both of the above, bout they're different

## Handling errors
Try fetching some different URIs with the `requests` module in your Python interpreter. More specifically, try some that don't work. Try some sites that don't exist, like http://bad.example.com/, but also try some pages that don't exist on sites that do, like http://google.com/ThisDoesNotExist.

What do you notice about the responses that you get back?
```
uri = "http://bad.example.com/"
r = requests.get(uri)
```

### Question 3 of 3
Using the requests module, try making GET requests to nonexistent sites or pages, e.g. http://bad.example.com or http://google.com/NotExisty. Mark all of the statements that are true:
- Accessing a nonexistent site raises a Python Exception.
- Accessing a nonexistent site gives you an object `r` where `r.status_code` is an error code.
- Accessing a nonexistent page on a real site raises a Python exception.
- Accessing a nonexistent page on a real site gives you an object `r` where `r.status_code` is an error code.