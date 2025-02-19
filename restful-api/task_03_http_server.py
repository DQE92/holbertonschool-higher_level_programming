#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler for implementing a basic REST API.
    
    This handler supports GET requests and returns responses in both plain text
    and JSON format depending on the endpoint. It includes basic error handling
    and CORS support.
    
    Endpoints:
        /: Returns a welcome message
        /data: Returns sample JSON data
        /status: Returns API status
        /info: Returns API information and available endpoints
    """

    def send_json_response(self, data):
        """
        Send a JSON response to the client.
        
        Args:
            data (dict): The data to be sent as JSON
        
        Note:
            This method automatically handles JSON conversion and sets appropriate headers
            including CORS headers for cross-origin requests.
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Pour CORS
        self.end_headers()
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def send_error_response(self, message, status_code=404):
        """
        Send an error response to the client.
        
        Args:
            message (str): The error message to be sent
            status_code (int, optional): The HTTP status code. Defaults to 404.
        
        Note:
            The error response includes the timestamp and the requested path
            for debugging purposes.
        """
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error_data = {
            "error": message,
            "timestamp": datetime.now().isoformat(),
            "path": self.path
        }
        self.wfile.write(bytes(json.dumps(error_data), "utf-8"))

    def do_GET(self):
        """
        Handle GET requests.
        
        This method routes requests to different handlers based on the requested path.
        It implements the following endpoints:
        - /: Returns a welcome message
        - /data: Returns a sample JSON dataset
        - /status: Returns the API status
        - /info: Returns API information
        
        Any undefined paths return a 404 error.
        
        Raises:
            Exception: Any unhandled exceptions are caught and return a 500 error
        """
        try:
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))
                
            elif self.path == '/data':
                data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self.send_json_response(data)
                
            elif self.path == '/status':
                self.send_json_response({"status": "OK"})
                
            elif self.path == '/info':
                info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server",
                    "endpoints": ["/", "/data", "/status", "/info"]
                }
                self.send_json_response(info)
                
            else:
                self.send_error_response("Endpoint not found")
                
        except Exception as e:
            self.send_error_response(str(e), 500)

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Run the HTTP server.
    
    Args:
        server_class: The HTTP server class to use (default: HTTPServer)
        handler_class: The request handler class (default: SimpleAPIHandler)
        port (int): The port to listen on (default: 8000)
    
    Note:
        The server runs until interrupted with Ctrl+C. It handles keyboard
        interrupts gracefully and shuts down the server properly.
    
    Raises:
        Exception: Any unhandled exceptions during server startup are caught
                  and logged.
    """
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f"Starting server on port {port}...")
        print(f"Available endpoints: /, /data, /status, /info")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == '__main__':
    run()
