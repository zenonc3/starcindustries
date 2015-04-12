
#NOTE: You will have to update the ip address in index.html
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import datetime
from MotionProcessor import MotionProc


period_loop = ''

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print 'new connection'
    self.write_message("Hi, client: connection is made ...")
    global period_loop
    global mproc
    mproc.set_callback(self.test)
#    period_loop = tornado.ioloop.PeriodicCallback(self.test, 500)
#    period_loop.start()
#    tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=5), self.test)

  def on_message(self, message):
    print 'message received: \"%s\"' % message
    self.write_message("Echo: \"" + message + "\"")
    if (message == "green"):
      self.write_message("green!")

  def on_close(self):
    print 'connection closed'
#    period_loop.stop()
    
  def test(self, action):
    
#    global mproc
#    print mproc.get_action()
    self.write_message(str(action))
             
  def check_origin(self, origin):
    return True


application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])




if __name__ == "__main__":
  
  mproc = MotionProc()
  t = threading.Thread(target=mproc.gesture_loop)
  print 'thread created'
  t.daemon = True
  t.start()
  print 'thread started'
  
  application.listen(9090)
  main_loop = tornado.ioloop.IOLoop.instance()
  main_loop.start()

#  while True:
#    pass