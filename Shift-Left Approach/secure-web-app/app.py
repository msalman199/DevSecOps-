from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Vulnerable SQL query (for demonstration)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vulnerable SQL injection point
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        # This is intentionally vulnerable for testing purposes
        
        return f"Query executed: {query}"
    
    return '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/')
def home():
    return '<h1>Secure Web App Demo</h1><a href="/login">Login</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
