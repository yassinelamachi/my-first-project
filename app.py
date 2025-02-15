import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

# Connect to MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Pochita17$',  # Replace with your MySQL root password
        database='my_project_db'
    )
    return conn

# Route to fetch users
@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users_data)

if __name__ == '__main__':
    app.run(debug=True)