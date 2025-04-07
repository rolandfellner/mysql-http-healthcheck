from flask import Flask
import pymysql
import os

app = Flask(__name__)

# Load DB config from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "kuma_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "yourStrongPass")
DB_NAME = os.getenv("DB_NAME", "kuma_monitoring")
DB_TIMEOUT = int(os.getenv("DB_TIMEOUT", 3))

@app.route('/health')
def healthz():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connect_timeout=DB_TIMEOUT
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW();")
        return "OK", 200
    except Exception as e:
        return f"DB Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)