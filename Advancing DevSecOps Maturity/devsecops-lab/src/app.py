from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Intentionally vulnerable code for demonstration
@app.route('/')
def home():
    return '''
    <h1>DevSecOps Demo Application</h1>
    <form action="/search" method="post">
        <input type="text" name="query" placeholder="Search users">
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # Vulnerable SQL query (for demonstration)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    sql = f"SELECT * FROM users WHERE name LIKE '%{query}%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    
    return f"<h2>Search Results:</h2><p>{results}</p>"

@app.route('/admin')
def admin():
    # Hardcoded credentials (vulnerability)
    admin_password = "admin123"
    return f"Admin panel - Password: {admin_password}"

if __name__ == '__main__':
    # Create sample database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                     (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'John Doe', 'john@example.com')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'Jane Smith', 'jane@example.com')")
    conn.commit()
    conn.close()
    
    app.run(host='0.0.0.0', port=5000, debug=True)
