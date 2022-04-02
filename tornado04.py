# 监听变化得端口
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import web
# 全局参数定义、存储、转换
from tornado.options import options

# options.parse_config_file(path)  # 获取参数的方法，从配置文件导入
# 此时的配置文件需要严格按照python语法要求来写，不支持字典类型
# 定义两个参数，该参数可通过命令行或配置文件赋值
options.define(name='port', default=8000, type=int, help='this is a port', multiple=False)
options.define(name='list', default=[], type=str, multiple=True)  # 列表里元素类型为str


class TestHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World!")


if __name__ == "__main__":
    # 关闭登录日志
    # options.logging = None
    # 创建一个名为config的普通文件
    options.parse_config_file("config")

    print('list=', options.list)
    app = web.Application([
        (r"/", TestHandler),
    ])
    # app.listen(8000)

    # （创建服务器）实例化一个http服务器对象 HTTPServer需要到app中匹配路由
    httpServer = HTTPServer(app)
    # (服务器端口)绑定端口
    # 使用变量的值
    httpServer.bind(options.port)
    httpServer.start(1)
    # tornado默认启动单进程
    IOLoop.current().start()
