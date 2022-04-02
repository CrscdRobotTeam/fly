# 监听变化得端口
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import web
# 全局参数定义、存储、转换
from tornado.options import options

# 创建config.py文件，当成模块导入
import config



class TestHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World!")


if __name__ == "__main__":

    print('list=', config.options["list"])
    app = web.Application([
        (r"/", TestHandler),
    ])
    # app.listen(8000)

    # （创建服务器）实例化一个http服务器对象 HTTPServer需要到app中匹配路由
    httpServer = HTTPServer(app)
    # (服务器端口)绑定端口
    # 使用变量的值
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    # tornado默认启动单进程
    IOLoop.current().start()
'''
如使用parse_command_line()或者parse_config_file(path)方法时，tornado会默认开启logging模块，向屏幕终端输入一些打印信息
'''