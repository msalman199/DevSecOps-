#!/usr/bin/env python3

import json
import os
from datetime import datetime

def generate_security_dashboard():
    """Generate a comprehensive security dashboard"""
    
    dashboard_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Security Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .header { background-color: #2c3e50; color: white; padding: 20px; text-align: center; }
            .section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
            .pass { background-color: #d4edda; border-color: #c3e6cb; }
            .fail { background-color: #f8d7da; border-color: #f5c6cb; }
            .warning { background-color: #fff3cd; border-color: #ffeaa7; }
            .metric { display: inline-block; margin: 10px; padding: 10px; border-radius: 5px; min-width: 150px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>DevSecOps Security Dashboard</h1>
            <p>Generated on: {timestamp}</p>
        </div>
        
        <div class="section">
            <h2>Security Scan Summary</h2>
            <div class="metric pass">
                <h3>SAST Scan</h3>
                <p>Status: {sast_status}</p>
            </div>
            <div class="metric warning">
                <h3>Dependency Scan</h3>
                <p>Status: {dependency_status}</p>
            </div>
            <div class="metric fail">
                <h3>Security Tests</h3>
                <p>Status: {security_test_status}</p>
            </div>
        </div>
        
        <div class="section">
            <h2>Compliance Status</h2>
            <div class="metric warning">
                <h3>OpenSCAP Compliance</h3>
                <p>Status: {compliance_status}</p>
            </div>
            <div class="metric pass">
                <h3>Privacy Compliance</h3>
                <p>Status: {privacy_status}</p>
            </div>
        </div>
        
        <div class="section">
            <h2>Threat Model Status</h2>
            <p><strong>LINDDUN Analysis:</strong> Completed</p>
            <p><strong>OWASP Threat Dragon:</strong> Model Created</p>
            <p><strong>Critical Threats Identified:</strong> 5</p>
            <p><strong>Mitigations Implemented:</strong> 3</p>
        </div>
        
        <div class="section">
            <h2>Recommendations</h2>
            <ul>
                <li>Implement stronger password hashing (replace MD5 with bcrypt)</li>
                <li>Add input validation to prevent SQL injection</li>
                <li>Implement rate limiting for authentication endpoints</li>
                <li>Add comprehensive audit logging</li>
                <li>Implement HTTPS/TLS encryption</li>
            </ul>
        </div>
    </body>
    </html>
    """.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        sast_status="Completed with warnings",
        dependency_status="Vulnerabilities found",
        security_test_status="Failed - Security issues detected",
        compliance_status="Partial compliance",
        privacy_status="Compliant"
    )
    
    with open('security_dashboard.html', 'w') as f:
        f.write(dashboard_html)
    
    print("Security dashboard generated: security_dashboard.html")

if __name__ == "__main__":
    generate_security_dashboard()
