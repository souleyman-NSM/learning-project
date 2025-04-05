from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Connexion à PostgreSQL (grâce aux variables d'environnement)
def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Connexion réussie à PostgreSQL ! Version : {db_version[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
