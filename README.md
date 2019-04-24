## Python Web Server

I will develop a simple Web server in Python that is capable of processing multi-requests using threads. Specifically, my Web server will:

* create a connection socket when contacted by a client (browser);
* receive the HTTP request from this connection;
* parse the request to determine the specific file being requested;
* get the requested file from the server’s file system;
* create an HTTP response message consisting of the requested file preceded by header lines; and
* send the response over the TCP connection to the requesting browser. 

If a browser requests a file that is not present in my server, my server should return a “404 Not Found” error message.
Run my server, and then test my server by sending requests from browsers running on different hosts. If you run my server on a host that already has a Web server running on it, then you should use a different port than port 80 for my Web server.
