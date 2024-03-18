from app import  app
from app.config import Config
from flup.server.fcgi import WSGIServer
from flask_cors import CORS

CORS(app, resources=r'/*')

if __name__ == '__main__':

    if(Config.DEBUG):
        app.run(host='127.0.0.1', port=Config.HTTP_PORT, debug=Config.DEBUG)
    else:
        WSGIServer(app,bindAddress=('127.0.0.1',Config.HTTP_PORT)).run()