# GET and POST

## Form methods: GET and POST

In the last lesson, I mentioned that GET is only one of many HTTP verbs or methods.

When a browser submits a form via `GET`, it puts all of the form fields into the URI that it sends to the server. These are sent as a query, in the request path — just like search engines do. They're all jammed together into a single line. Since they're in the URI, the user can bookmark the resulting page, reload it, and so forth.

This is fine for search engine queries, but it's not quite what we would want for (say) a form that adds an item to your shopping cart on an e-commerce site, or posts a new message on a comments board. `GET` methods are good for search forms and other actions that are intended to look something up or ask the server for a copy of some resource. But `GET` is not recommended for actions that are intended to alter or create a resource. For this sort of action, HTTP has a different verb, `POST`.


## Idempotence

Vocabulary word of the day: **idempotent**. An action is idempotent if doing it twice (or more) produces the same result as doing it once. "Show me the search results for 'polar bear'" is an idempotent action, because doing it a second time just shows you the same results. "Add a polar bear to my shopping cart" is not, because if you do it twice, you end up with two polar bears.

`POST` requests are not idempotent. If you've ever seen a warning from your browser asking you if you really mean to resubmit a form, what it's really asking is if you want to do a non-idempotent action a second time.

(Important note if you're ever asked about this in a job interview: idempotent is pronounced like "eye-dem-poe-tent", or rhyming with "Hide 'em, Joe Tent" — not like "id impotent".)


### Exercise: Be a server and receive a POST request

Here's a piece of HTML with a form in it that is submitted via POST:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Testing POST requests</title>
    <style>
        label, input, button {
            margin: 8px;
        }
    </style>
</head>
<body>
    <form action="http://localhost:9999/" method="POST">
        <label>Magic input:
            <input type="text" name="magic" value="mystery">
        </label>
        <br>
        <label>Secret input:
                <input type="text" name="secret" value="spooky">
        </label>
        <br>
        <button type="submit">Do a thing!</button>
    </form>
</body>
</html>
```

This form is in your exercises directory as `Lesson-2/2_HTMLForms/PostForm.html`.

-    Open it up in your browser. You should see a form.
-    Don't submit that form just yet.
-    First, open up a terminal and use `ncat -l 9999` to listen on port 9999.
-    Then type some words into the form fields in your browser, and submit the form.

You should see an HTTP request in your terminal. Take a careful look at this request!


When a browser submits a form as a POST request, it doesn't encode the form data in the URI path, the way it does with a GET request. Instead, it sends the form data in the request body, underneath the headers. The request also includes `Content-Type` and `Content-Length` headers, which we've previously only seen on HTTP responses.

> By the way, the names of HTTP headers are case-insensitive. So there's no difference between writing `Content-Length` or `content-length` or even `ConTent-LeNgTh` … except, of course, that humans will read your code and be confused by that last one.

