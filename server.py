from cheroot.wsgi import Server
from titan_app import app


server = Server(('0.0.0.0', 1010), app)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()
