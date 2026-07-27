from flask import Flask, request, render_template_string
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def home():
    return '''
    <h1>DevSecOps Demo Application (Secured)</h1>
    <form action="/search" method="post">
        <input type="text" name="query" placeholder="Search users">
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # Secure parameterized query
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f'%{query}%',))
    results = cursor.fetchall()
    conn.close()
    
    return f"<h2>Search Results:</h2><p>{results}</p>"

@app.route('/admin')
def admin():
    # Remove hardcoded credentials
    return "Admin panel - Please authenticate properly"

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
    
    # Remove debug mode for production
    app.run(host='0.0.0.0', port=5000, debug=False)
