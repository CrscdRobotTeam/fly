# 开启多进程
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
    # app.listen(8000)# 只能在单进程中使用

    # （创建服务器）实例化一个http服务器对象 HTTPServer需要到app中匹配路由
    httpServer = HTTPServer(app)
    # (服务器端口)绑定端口（单进程）
    # httpServer.listen(8000)

    # tornado启动多进程,将服务器绑定到固定端口
    httpServer.bind(8000)
    httpServer.start(5)  # 默认开启1个进程（）或（1），
    # 值大于0，创建对应个数的子进程，值可为None或者为负数则开启对应硬件机器cpu核心数个子进程
    ioloop.IOLoop.current().start()

    '''
    虽然tornado提供了一次性启动多个进程的方式，
    但是由于一些问题，不建议使用 bind+ start方式启动多进程
    而是，手动启动多个进程，并且还能绑定不同的端口
    '''

    '''
    问题：
    1.每个子进程都会从父进程中复制一份IOLoop的实例
    如果在创建子进程前修改IOLoop，所有子进程IOLoop会受到影响
    2.所有进程都是一个命令启动的（一个进程，启动所有子进程），
    无法在不停止服务的情况下修改子进程代码
    3.子进程共享一个端口，想要分别监控很困难
    '''
