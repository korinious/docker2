from flask import Flask
from redis import Redis, RedisError
import os
import socket
redis = Redis(host="docker-redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Ooops! Connection could not be established!</i>"
html = "<h3>Yeah! Docker leme kai (den) klaime! Ok, isws.</h3>\n" \
           "<b>Hostname:</b> {hostname}<br/>\n" \
           "<b>How many times:</b> {visits}\n"
return html.format(hostname=socket.gethostname(), visits=visits)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)