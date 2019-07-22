## Handling more requests

Try creating a link in it where the target URI is the bookmark server's own URI. What happens when you try to do that?
Looking at the bookmark server I've deployed on Heroku.

Looking at the bookmark server I've deployed on Heroku.
I'm about to submit the bookmark server's own URI in the form.

When I do this, the app gives me an error, saying it can't fetch that web page. That's weird! The server is right there; it should be able to reach itself! What do you think is going on here?

Why can't the bookmark server fetch a page from itself?
* **http.server can only handle one request at a time.**

That's right! The basic, built-in http.server.HTTPServer class can only handle a single request at once. The bookmark server tries to fetch every URI that we give it, while it's in the middle of handling the form submission.

It's like an old-school telephone that can only have one call at once. Because it can only handle one request at a time, it can't "pick up" the second request until it's done with the first … but in order to answer the first request, it needs the response from the second.

### Concurrency

Being able to handle two ongoing tasks at the same time is called concurrency, and the basic http.server.HTTPServer doesn't have it. It's pretty straightforward to plug concurrency support into an HTTPServer, though. The Python standard library supports doing this by adding a mixin to the HTTPServer class. A mixin is a sort of helper class, one that adds extra behavior the original class did not have. To do this, you'll need to add this code to your bookmark server:

```python
import threading
from socketserver import ThreadingMixIn
```

```python
class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."
```

Then look at the bottom of your bookmark server code, where it creates an HTTPServer. Have it create a ThreadHTTPServer instead:`

```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, Shortener)
    httpd.serve_forever()
```

Commit this change to your Git repository, and push it to Heroku. Now when you test it out, you should be able to add an entry that points to the service itself.
Question 2 of 2

Try posting an entry to your bookmark server that points to the server itself now. Did it work? If so, the server is now able to handle a second incoming request while processing another request.