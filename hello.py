
from flask import Flask, session
#from datetime import timedelta
import time
app = Flask(__name__)

#@app.before_request
#def set_session_timeout():
 #   session.permanent = True
  #  app.permanent_session_lifetime = timedelta(minutes=1)


@app.route("/")
def hello():
    print("hello")
    time.sleep(10)
    print("hello 10")
    return "Hello World!"

if __name__ == "__main__":
    app.run('0.0.0.0',9595)
