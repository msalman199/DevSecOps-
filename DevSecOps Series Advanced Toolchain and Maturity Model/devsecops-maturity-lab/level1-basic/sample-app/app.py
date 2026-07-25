from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Intentionally vulnerable code for demonstration
@app.route('/')
def home():
    return '<h1>Sample Application - Level 1</h1><a href="/search">Search Users</a>'

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # SQL Injection vulnerability (intentional for demo)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name LIKE '%{query}%'")
    results = cursor.fetchall()
    conn.close()
    return f"Results: {results}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
