from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json
import pprint
import cgi

json1 = {"key": "value"}
json2 = {"key1": "value1"}

class MyRequestHandler (BaseHTTPRequestHandler) :

    def do_GET(self) :

        if self.path == "/json1" :
            #send response code:
            self.send_response(200)
            #send headers:
            self.send_header("Content-type:", "text/html")
            # send a blank line to end headers:
            self.wfile.write("\n")

            #send response:
            json.dump(json1, self.wfile)

        elif self.path == "/json2" :
            #send response code:
            self.send_response(200)
            #send headers:
            self.send_header("Content-type:", "text/html")
            # send a blank line to end headers:
            self.wfile.write("\n")

            #send response:
            json.dump(json2, self.wfile)
    def do_POST(se) :

        if se.path == "/json1" :
            print '------->',se.headers
            #send response code:
            se.send_response(200)
            #send headers:
            se.send_header("Content-type:", "text/html")
            # send a blank line to end headers:
            se.wfile.write("\n")

            #send response:
            json.dump(json1, se.wfile)
            ctype, pdict = cgi.parse_header(se.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                postvars = cgi.parse_multipart(se.rfile, pdict)
            elif ctype == 'application/x-www-form-urlencoded':
                length = int(self.headers.getheader('content-length'))
                postvars = cgi.parse_qs(se.rfile.read(length), keep_blank_values=1)
            else:
                postvars = {}
        print postvars
server = HTTPServer(("localhost", 8003), MyRequestHandler)

server.serve_forever()

