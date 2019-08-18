# HTML Forms

### Exercise: HTML and forms

Dust off your HTML knowledge and let's take a look at a form that gets submitted to a server.

If you need a refresher on HTML forms, take a look at the MDN introduction (gentle) or the W3C standard reference (more advanced).

Here's a piece of HTML that contains a form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login Page</title>
    <style>
        label, input, button {
            margin: 8px;
        }
    </style>
</head>
<body>
    <form action="http://localhost:8000/" method="GET">
        <h2>Login</h2>
        <label for="username">Username:</label>
        <input type="text" name="username" id="username">
        <br>
        <label for="pw">Password:</label>
        <input type="password" name="pw" id="pw">
        <br>
        <button type=submit>Log in!</button>
    </form>
</body>
</html>

```

This HTML is also in the exercises directory, under `Lesson-2/2_HTMLForms/LoginPage.html`. Open it up in your browser.

Before pressing the submit button, start up the **echo server** again on port 8000 so you can see the results of submitting the form.


Exercise: Form up for action

Let's do another example! This HTML form has a pull-down menu with four options.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Search wizardry!</title>
    <style>
        label, input, button {
            margin: 8px;
        }
    </style>
</head>
<body>

    <form action="http://www.google.com/search" method="GET">
        <label>Search term:
            <input type="text" name="q">
        </label>
        <br>
        <label>Corpus:
            <select name="tbm">
                <option selected value="">Regular</option>
                <option value="isch">Images</option>
                <option value="bks">Books</option>
                <option value="nws">News</option>
            </select>
        </label>
        <br>
        <button type="submit">Go go!</button>
    </form>
</body>
</html>
```

This form is in the HTML file `SearchPage.html` in the same directory. Open it up in your browser.

This form tells your browser to submit it to Google Search. The inputs in the form supply the `q` and `tbm` query parameters. (And if Google ever changes the way their search query parameters work, this example is going to be totally broken.)
