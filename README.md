# PyServer
Minimal server with python

<pre>
Launch :
$ ./serv.py
127.0.0.1 - - [21/Oct/2016 10:04:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [21/Oct/2016 10:04:02] "GET /youhou HTTP/1.1" 404 -
127.0.0.1 - - [21/Oct/2016 10:04:06] "GET /query?period=today HTTP/1.1" 200 -
{'period': ['today']}
127.0.0.1 - - [21/Oct/2016 10:04:10] "GET /query?period=today&account=TOTO HTTP/1.1" 200 -
{'account': ['TOTO'], 'period': ['today']}

$ curl -q "http://localhost:8000"
hello world

$ curl -q "http://localhost:8000/youhou"
bye

$ curl -q "http://localhost:8000/query?period=today"
{"result": [], "error": "Missing parameter"}

$ curl -q "http://localhost:8000/query?period=today&account=TOTO"
{"result": ["Something for TOTO"], "error": null}
</pre>
