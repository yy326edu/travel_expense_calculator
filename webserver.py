# -*- coding:utf-8 -*-
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import sys

from main import app
reload(sys)
sys.setdefaultencoding('utf-8')


http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8082)  # 默认端口
IOLoop.instance().start()
