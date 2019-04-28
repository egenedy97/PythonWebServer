#!/usr/bin/env python3 
''' 
    author : Genedy 
'''
import httpserver 
s_address = '0.0.0.0'
port = 8000
if __name__ == "__main__":
    httpd = httpserver.HttpServer(s_address,port) 
    while True:
        httpd.serve()

