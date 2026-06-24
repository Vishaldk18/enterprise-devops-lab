from flask import Flask, jsonify
import redis
import os
import socket
 
app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
 
ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")
VERSION = os.getenv("VERSION", "1.0.0")

try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
except Exception:
    r = None

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/visitor-count")
def visitor_count():
 
    hostname = socket.gethostname()
 
    try:
        count = r.incr("visitor_count")
 
        redis_status = "Connected"
 
    except Exception:
 
        count = 0
 
        redis_status = "Disconnected"
 
    return jsonify({
        "count": count,
        "hostname": hostname,
        "environment": ENVIRONMENT,
        "version": VERSION,
        "redis": redis_status
    })

@app.route("/")
def home():
 
    return jsonify({
        "message": "Welcome to Enterprise DevOps Lab"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
