from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape

import models
import variables


class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self) -> None:
        if self.path.startswith('/static/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()
        elif self.path == '/about/':
            self.render_about()
        elif self.path == '/blog/':
            self.render_blog()
        elif self.path.startswith('/blog-single/'):
            try:
                id = int(self.path[self.path.rfind("/") + 1:])
                blog = list(filter(lambda i: i.id == id, models.Blog.fetch_all()))[0]
                self.render_single_blog(blog)
            except:
                self.render_404()

    def render_index(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template("index.html").render(products=models.Product.fetch_all(),
                                                          reviews=models.Recommendation.fetch_all(),
                                                          features=variables.features)
        self.wfile.write(body.encode("utf-8"))

    def render_about(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template("about.html").render(title='about', reviews=models.Recommendation.fetch_all(),
                                                          features=variables.features)
        self.wfile.write(body.encode("utf-8"))

    def render_blog(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template("blog.html").render(title='blog', blogs=models.Blog.fetch_all(),
                                                         instagramm=variables.instagram,
                                                         tags=models.Tag.fetch_all(),
                                                         categories=models.Category.fetch_all())
        self.wfile.write(body.encode("utf-8"))

    def render_single_blog(self, blog):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template("single-blog.html").render(title='blog-single', blog=blog,
                                                                blogs=models.Blog.fetch_all(),
                                                                instagramm=variables.instagram,
                                                                tags=models.Tag.fetch_all(),
                                                                comments=models.Comment.fetch_all(),
                                                                categories=models.Category.fetch_all())
        self.wfile.write(body.encode("utf-8"))

    def render_404(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template("404.html").render()
        self.wfile.write(body.encode("utf-8"))
