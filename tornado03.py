# 监听变化得端口
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import web
# 全局参数定义、存储、转换
from tornado.options import options

# 一个函数说，原型、功能、参数，确定该函数
'''
1.options.define()
函数原型：options.define(name='',default=None,type=None,help=None,metavar=None,multiple=False,group=None,callback=None)
函数功能：用来定义options选项变量的定义
函数参数：1）name:函数变量名，必须保证其唯一性，否则会报 “Options 'XXX' already define in ...”
         default:设置选项默认值，如果不设置默认为None
         
         2）type:设置选项变量的类型,从命令行或配置文件导入参数时tornado会根据类型转换输入的值，
         转换不成会报错 str、float、datetime、int,如果没有设置，会根据default值转换，如果default没设置，则不进行转换
         
         3）multiple:设置变量是否可以为多个值，默认为false
         
         4）help：选线变量的帮助提示信息
         
2.options.options 全局options对象，所有定义的选项变量都会作为该对象的变量
3.options.parse_command_line() 获取参数的方法，转换命令行参数
4.options.parse_config_file(path) 获取参数的方法，从配置文件导入

'''
# 定义两个参数，该参数可通过命令行或配置文件赋值
options.define(name='port', default=8000, type=int, help='this is a port', multiple=False)
options.define(name='list', default=[], type=str,multiple=True)  # 列表里元素类型为str


class TestHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World!")


if __name__ == "__main__":
    # 转换命令行参数，并保存到tornado.options.options
    options.parse_command_line()  # 不用任何参数，把命令行参数，转到options中，从而转换到程序中
    # 关闭log在终端输入 -- logging=None
    # 黑终端输入 python tornado03.py --port=9000 --list=good,nice --logging=none
    print('list=',options.list)
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
