#!/usr/bin/env python3
"""
Sample application for DevSecOps lab
"""
import os
import boto3
from flask import Flask, jsonify

app = Flask(__name__)

# Intentional security issues for demonstration
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # Hard-coded credential (bad practice)
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Hard-coded credential

@app.route('/')
def hello():
    return jsonify({"message": "Hello from DevSecOps Lab!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/data')
def get_data():
    # Intentional SQL injection vulnerability for demonstration
    user_id = request.args.get('user_id')
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection risk
    return jsonify({"query": query})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Debug mode in production (bad practice)
