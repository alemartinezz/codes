# Printf and Nectat

**Quiz-what-web-server-does-Google-use**

```git
printf 'HEAD / HTTP/1.1\r\nHost: en.wikipedia.org\r\n\r\n' | nc en.wikipedia.org 80
```

## Output

```git
HTTP/1.1 200 OK
Date: Tue, 09 Apr 2019 16:26:09 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2019-04-09-16; expires=Thu, 09-May-2019 16:26:09 GMT; path=/; domain=.google.com
Set-Cookie: NID=180=ymeCmr7_5ZmDRumi5Lk7DLiD0YqdribzuMfatmN4rhVQdHQjrVYhJXc5kN2I7dXJWWoBHA2wy50qQkXJr6uqWO8SWBV4_fDX8vDjmdV1JQwWGj_Cj_vxR8ZJvZxpuSni5fx1UrGXZOMLZrdonXRnk1xqauM-OU7Iwvcoiej_HGU; expires=Wed, 09-Oct-2019 16:26:09 GMT; path=/; domain=.google.com; HttpOnly
Transfer-Encoding: chunked
Accept-Ranges: none
Vary: Accept-Encoding
```

Netcat connects to a port, and sends a string over it. The server sends the HTTP response.