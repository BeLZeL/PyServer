#!/usr/bin/python2

import BaseHTTPServer
import urlparse
import json

class httpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "r") as source_fh:
                self.wfile.write(source_fh.read())
            self.wfile.close()
            
        elif self.path.startswith("/query?"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            url = urlparse.urlparse(self.path)
            request_items = urlparse.parse_qs(url.query)
            print(request_items)
            response = {"error": None, "result": []}
            if not request_items["period"][0] in ["today", "3days", "1week"]:
                response["error"] = "Invalid period"
            elif not "account" in request_items and not "order_id" in request_items:
                response["error"] = "Missing parameter"
            else:
                response["result"] = ["Something for %s" % ( request_items["account"][0] ) ]
            self.wfile.write(json.dumps(response))
            self.wfile.close()
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("bye\n")
            self.wfile.close()

if __name__ == "__main__":
    server_address = ('127.0.0.1', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, httpHandler)
    while True:
        httpd.handle_request()
