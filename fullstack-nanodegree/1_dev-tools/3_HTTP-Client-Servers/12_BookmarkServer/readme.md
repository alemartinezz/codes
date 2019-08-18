## Exercise: The bookmark server

You're almost to the end of this lesson! One more server to write …

You've probably seen URL-shortening services such as TinyURL.

They let you create short URI paths like https://tinyurl.com/jye5r6l that redirect to a longer URI on another site. It's easier to put a short URI into an email, text message, or tweet. In this exercise, you'll be writing a service similar to this.

Like the **messageboard** server, this **bookmark server** will keep all of its data in memory. This means that it'll be reset if you restart it.

Your server needs to do three things, depending on what kind of request it receives:

- On a GET request to the / path, it displays an HTML form with two fields. One field is where you put the **long URI** you want to shorten. The other is where you put the **short name** you want to use for it. Submitting this form sends a POST to the server.
- On a POST request, the server looks for the two form fields in the request body. If it has those, it first checks the URI with **requests.get** to make sure that it actually exists (returns a 200).
    - If the URI exists, the server stores a dictionary entry mapping the short name to the long URI, and returns an HTML page with a link to the short version.
     - If the URI doesn't actually exist, the server returns a 404 error page saying so.
    - If either of the two form fields is missing, the server returns a 400 error page saying so.
- On a GET request to an existing short URI, it looks up the corresponding long URI and serves a redirect to it.

The starter code for this exercise is in the `7_BookmarkServer` directory. I've given you a skeleton of the server; your job is to fill out the details!


### The bookmark server
Check off these steps as you complete them in the Bookmark Server exercise. After each step, try running the server and the test.py script to test it!

- Write the `CheckURI` function. This function should take a URI as an argument, and return `True` if that URI could be successfully fetched, and `False` if it can´t.
- Write the code inside `do_GET` that sends a 303 redirect to a known name.
- Write the code inside `do_POST` that sends a 400 error if the form fields are not present in the POST.
- Write the code inside `do_POST` that sends a 303 redirect to the form after saving a newly submitted URI.
- Write the code inside `do_POST` that sends a 404 error if a URI is not successfully checked (i.e. if CheckURI returns `false`)