from tornado.httpserver import HTTPServer
from tornado import ioloop
from tornado import web


class TestHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World!")


if __name__ == "__main__":
    app = web.Application([
        (r"/", TestHandler),
    ])
    # app.listen(8000)

    # （创建服务器）实例化一个http服务器对象 HTTPServer需要到app中匹配路由
    httpServer = HTTPServer(app)
    # (服务器端口)绑定端口
    httpServer.listen(8000)
    # tornado默认启动单进程
    ioloop.IOLoop.current().start()
