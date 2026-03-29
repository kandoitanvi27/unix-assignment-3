import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database configuration
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "tododb")
DB_USER = os.environ.get("DB_USER", "todouser")
DB_PASS = os.environ.get("DB_PASS", "todopass")


@app.route("/")
def index():
    return render_template("index.html", todos=[])


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
