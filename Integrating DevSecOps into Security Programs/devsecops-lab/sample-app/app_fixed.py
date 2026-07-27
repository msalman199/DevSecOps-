from flask import Flask, request, render_template_string, escape
import sqlite3
import os
import logging
import secrets
from datetime import datetime

# Configure secure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Secure secret key

# Security headers middleware
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/')
def home():
    return '''
    <h1>Secure DevSecOps Lab Application</h1>
    <p>This is a security-hardened version of the application.</p>
    <a href="/search">Search Users</a>
    '''

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # Input validation
    if len(query) > 100:
        return "Query too long", 400
    
    # Parameterized query to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ? LIMIT 10", (f'%{query}%',))
    results = cursor.fetchall()
    conn.close()
    
    # Secure template rendering with proper escaping
    safe_query = escape(query)
    template = f"<h2>Search Results for: {safe_query}</h2><ul>"
    
    for result in results:
        safe_name = escape(result[1])
        safe_email = escape(result[2])
        template += f"<li>{safe_name} ({safe_email})</li>"
    
    template += "</ul><a href='/'>Back to Home</a>"
    
    return template

if __name__ == '__main__':
    # Secure configuration
    app.run(debug=False, host='127.0.0.1', port=5000)
