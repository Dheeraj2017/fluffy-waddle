from flask import Flask

app = Flask(__name__)

from views import *;

if __name__=='__main__' :
        import os
        HOST=os.environ.get('SERVER_HOST','localhost')
        try:
              PORT=int(os.environ.get('SERVER_PORT',5999))
        except ValueError:
              PORT=5999
        app.run(HOST,PORT)
