from http.server import HTTPServer
from handler import *
from models import *


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    print("Server starting...")
    print('Creating tables...')
    for table in [Blog, Category, Tag, Comment, Recommendation, Product]:
        table.create_table()
        print('Table {} was created'.format(table.__name__))
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server started")
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=CustomHandler)
