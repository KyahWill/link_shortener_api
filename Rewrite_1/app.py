from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
serverPort = 8080
unique_codes = {}
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        url = "https://www.youtube.com"
        self.send_response(302)
        self.send_header('Location', url)
        self.end_headers()


    def do_POST(self):
        print(self.request)
        print(self.rfile.read(int(self.headers('content-length'))))
        json_str = {
            "message":"tests"
        }
        string = json.dumps(json_str)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(string.encode(encoding="utf_8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")