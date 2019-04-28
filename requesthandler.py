#!/usr/bin/env python3 

''' 
  author : Genedy    
'''

import time

class Handler:

    def __init__(self, conn, address , data, cwd):

        self.client_socket = conn   
        self.client_address = address     
        self.current_directory = cwd      
        self.request = data               
        self.method = self.getmethod()   
        self.path = self.getpath()       
        self.version = self.getversion()         
        self.response_content_type = "text/html; charset=UTF-8\\r\\n"   
        self.status_dict = {'200':'OK' , '404':'Not Found'}             
        self.response_version = "HTTP/1.1"                              
        self.respnse_date = "Date: "+time.asctime() + "\\r\\n"          
        self.response_server = "Server: my_server/1.0\\r\\n"  


    def validaterequest(self):
        
        if ( self.method == '\0' or self.path == '\0' or self.version == '\0'):
            return False

        return True



    def handlerequest(self):

        print( '        ' + str(self.client_address) + ' Handling HTTP Request ...     ' )
        print( '        Method : ' + self.method)
        print( '        Path   : ' + self.path)
        print( '        Http   : ' + self.version)

        if(self.method == 'GET'):
            self.onGet()
            
        elif (self.method == 'POST'):
            self.onPost()

    def onGet(self):

        html_page = '' 
        status = 404   

        try:
            if(self.path == '/'):  
                html_page = self.getfile(self.current_directory + self.path + "index.html")
                if(html_page != '\0'):
                    status = 200   
            else:  
                html_page = self.getfile(self.current_directory + self.path) 
                if(html_page != '\0'):
                    status = 200   

        finally:
            response = (self.response_version + ' ' + str(status) + ' '  + self.status_dict[str(status)] + "\\r\\n" + self.respnse_date + self.response_server + self.response_content_type +"\\r\\n") 
            if (status == 200):
                response = response + html_page
            self.client_socket.sendall(str.encode(response)) 
            print( 'request handled , conn closed ')
            self.client_socket.close() 

    def getmethod(self):
        if (not self.request.find('GET') == -1):
            return 'GET'

        if (not self.request.find('POST') == -1):
            return 'POST'

        else :
            return '\0'
            
    def getpath(self):

        index_from = self.getindex(0,'/', self.request)
        if(index_from == -1):
            return '\0'
        
        index_to = self.getindex(index_from, ' ',self.request) - 1

        if(index_to == -1):
            return '\0'

        return self.request[index_from : index_to + 1]

    def getversion(self):
        

        version_index = self.request.find('HTTP')
        if (version_index == -1):
            return '\0'
        
        return self.request[version_index : version_index + 8]


    def getindex(self,i,char,string):
        
        for x in range(i,len(string)):
            if(string[x] == char):
                return x

        return -1


    def getfile(self,file_path):
        try:
            fd = open(file_path,'r')
            return fd.read()
        except:
            return '\0'    