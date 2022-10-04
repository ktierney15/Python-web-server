from http.server import BaseHTTPRequestHandler, HTTPServer
import time


hostName = "localhost"
serverPort = 8080



class MyServer(BaseHTTPRequestHandler):
    # do_GET method is from BaseHTTPRequestHandler
    def do_GET(self): # what the response will be for a get request
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Generated Web Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort)) #Server is started

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close() #Executes when you hit a keyboard interrupt, closing the server
    print("Server stopped.")
