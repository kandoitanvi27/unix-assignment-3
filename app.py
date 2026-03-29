import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database configuration
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "tododb")
DB_USER = os.environ.get("DB_USER", "todouser")
DB_PASS = os.environ.get("DB_PASS", "todopass")


def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
    )
    return conn


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            done BOOLEAN DEFAULT FALSE
        )
        """
    )
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, done FROM todos ORDER BY id DESC")
    todos = [{"id": row[0], "title": row[1], "done": row[2]} for row in cur.fetchall()]
    cur.close()
    conn.close()
    return render_template("index.html", todos=todos)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
