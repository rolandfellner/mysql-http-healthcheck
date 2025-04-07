from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/health')
def health():
    try:
        conn = pymysql.connect(
            host="your-mysql-host",
            user="sql_user",
            password="yourStrongPass",
            database="sql_monitoring",
            connect_timeout=3
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW();")
        return "OK", 200
    except Exception as e:
        return f"DB Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)