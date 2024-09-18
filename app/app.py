from flask import Flask, send_from_directory
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return f'This page has been viewed {redis.get("hits").decode("utf-8")} times.'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

