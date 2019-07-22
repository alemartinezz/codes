# Using a JSON API

As a web developer, you will deal with data in a lot of different formats, especially when your code calls out to APIs provided by other developers. It's not uncommon for a large software system to have parts that deal with a dozen or more different data formats. Fortunately, usually, someone else has already written libraries to help you read and write these formats.

**JSON** is a data format based on the syntax of JavaScript, often used for web-based APIs. There are a lot of services that let you send HTTP queries and get back structured data in JSON format. You can read more about the JSON format at http://www.json.org/.

Python has a built-in `json` module; and as it happens, the `requests` module makes use of it. A `Response` object has a `.json` method; if the response data is JSON, you can call this method to translate the JSON data into a Python dictionary.

Try it out! Here, I'm using it to access the Star Wars API, a classic JSON demonstration that contains information about characters and settings in the Star Wars movies:

```python
>>> a = requests.get('http://swapi.co/api/people/1/')
>>> a.json()['name']
'Luke Skywalker'
```

### Quiz Question
What happens if you call `r.json()` on a `Response` that isn't made of JSON data, such as the Udacity main page?

- It returns an empty dictionary.
- It raises an exception defined in Python's `json` library.
- It raises AttributeError; the method is only defined on valid JSON responses.
- It returns a dictionary containing a string which is the response data.


Toggle Sidebar
Using a JSON API
Using a JSON API

As a web developer, you will deal with data in a lot of different formats, especially when your code calls out to APIs provided by other developers. It's not uncommon for a large software system to have parts that deal with a dozen or more different data formats. Fortunately, usually, someone else has already written libraries to help you read and write these formats.
Using a JSON API

JSON is a data format based on the syntax of JavaScript, often used for web-based APIs. There are a lot of services that let you send HTTP queries and get back structured data in JSON format. You can read more about the JSON format at http://www.json.org/.

Python has a built-in json module; and as it happens, the requests module makes use of it. A Response object has a .json method; if the response data is JSON, you can call this method to translate the JSON data into a Python dictionary.

Try it out! Here, I'm using it to access the Star Wars API, a classic JSON demonstration that contains information about characters and settings in the Star Wars movies:
```python
>>> a = requests.get('http://swapi.co/api/people/1/')
>>> a.json()['name']
'Luke Skywalker'
```

### Quiz Question
What happens if you call r.json() on a Response that isn't made of JSON data, such as the Udacity main page?

## Extract data from a JSON response

There's a great example of an API on the site http://uinames.com/, a service that makes up fake names and user account information. You can find the full API documentation under the little menu at the top right.

For this exercise, all you'll need is this URI and a couple of query parameters:

http://uinames.com/api/

The query parameters to use are `ext`, which gives you a record with more fields, and `region`, which lets you specify which country you want your imaginary person to come from. For instance, to have the API invent a person from Italy:

http://uinames.com/api?ext&region=Italy

(It's not perfect. For instance, currently it makes up North American phone numbers for everyone, regardless of where they live.)


## Exercise: Use JSON with UINames.com

The starter code for this exercise is in the` Lesson-2/6_UsingJSON` directory, with the filename `UINames.py`. In this exercise, use the JSON methods described above to decode the response from the **uinames.com** site.

### Use JSON with UINames.com

Check off these steps as you complete them in the exercise.

- Decode the JSON data returned by the `GET` request.
- Print out the JSON data fields in the specified format.
- Test your code by running `UINames.py`.
- Run the test script in `test.py`