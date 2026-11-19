import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.get("/")
def index():
    return f"Hits: {cache.incr('hits')}\n"
