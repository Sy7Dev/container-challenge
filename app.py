from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/count")
def count():
    visit_count = redis_client.incr("visits")

    return render_template(
        "index.html",
        visit_count=visit_count
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
