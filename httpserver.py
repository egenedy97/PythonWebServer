#!/usr/bin/env python3 

''' 
    author : Genedy 
'''

import socket
import threading
import requesthandler
import os
import sys
import time

class HttpServer:
    
    def __init__(self,s_address,port,cwd=os.getcwd()):
        self.wd= cwd + '/html'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket = (s_address, port)
        print(" Server is On " + str(server_socket) + "  "  + str(time.asctime())   )
        try:
            self.sock.bind(server_socket)
        except Exception: 
            print('Server can not start on Port ' + str(port) + " ... exit")
            sys.exit() 
        self.sock.listen(50)
        
    def serve(self):

        try:
            connection, client_address = self.sock.accept()  
            print(" connection recv From " + str(client_address) )
            threading.Thread(target=self.dispatch , args=(connection,client_address)).start()  

        except KeyboardInterrupt: 
            print('Keyboard Interrupt ****** exit')
            self.sock.close()    
            sys.exit()

    def dispatch(self,client_socket,client_address):

        data = client_socket.recv(1024) 
        handler = requesthandler.Handler(client_socket,client_address,str(data),self.wd) 
        if(handler.validaterequest()): 
            handler.handlerequest()  



