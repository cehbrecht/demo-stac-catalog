#!/usr/bin/env python3
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class CorsStaticHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    handler = partial(CorsStaticHandler, directory="public")
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Serving demo STAC catalog at http://{host}:{port}/catalog/catalog.json")
    server.serve_forever()
