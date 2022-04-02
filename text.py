# -*- coding:utf-8 -*-

from tornado import web, ioloop

import datetime


class MainHandler(web.RequestHandler):
    def __init__(self,ag):
        self.ag=ag
    def get(self):
        self.finish('Hello Tornado %s'%self.ag)



def f2s():
    # print '2s ', datetime.datetime.now()
    main = MainHandler("f2")
    main.get()


def f5s():
    # print '5s ', datetime.datetime.now()

    main = MainHandler("f5")
    main.get()


if __name__ == '__main__':
    application = web.Application([

        (r'/', MainHandler),

    ])

    application.listen(8081)

    ioloop.PeriodicCallback(f2s, 2000).start()  # start scheduler 每隔2s执行一次f2s

    ioloop.PeriodicCallback(f5s, 5000).start()  # start scheduler 每隔5s执行一次f5s

    ioloop.IOLoop.instance().start()
