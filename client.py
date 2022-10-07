import http.client  
 
#get http server ip  
http_server = "localhost"
port = "8080"  
#create a connection  
conn = http.client.HTTPConnection(http_server, port)  
 
#request command to server  
conn.request("GET", http://localhost:8080)  
 
#get response from server  
rsp = conn.getresponse()  
 
#print server response and data  
print(rsp.status, rsp.reason)  
data_received = rsp.read()  
print(data_received)  
 
conn.close()  