__author__ = "那位先生Beer"
import tornado.ioloop
import tornado.web


class MainHandler( tornado.web.RequestHandler ):
    def get( self ):
        u=self.get_argument(name = "user")
        p=self.get_argument(name = "psw")
        self.write( str(u))

application = tornado.web.Application([
    (r"/index", MainHandler),
 ])

if __name__ == "__main__":
    application.listen( 8888 )
    tornado.ioloop.IOLoop.instance().start()