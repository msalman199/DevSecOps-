#!/usr/bin/env python3
"""
Security report generator for DevSecOps pipeline
"""
import json
import os
from datetime import datetime

def load_json_report(filename):
    """Load JSON report if it exists"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            return None
    return None

def generate_html_report():
    """Generate HTML security report"""
    
    # Load security scan results
    bandit_report = load_json_report('bandit-report.json')
    safety_report = load_json_report('safety-report.json')
    checkov_report = load_json_report('checkov-report.json')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Security Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
            .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
            .critical {{ background-color: #ffebee; }}
            .warning {{ background-color: #fff3e0; }}
            .info {{ background-color: #e8f5e8; }}
            .summary {{ font-size: 18px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>DevSecOps Security Scan Report</h1>
            <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="section info">
            <h2>Scan Summary</h2>
            <div class="summary">
                <p>✓ Static Application Security Testing (SAST) - Bandit</p>
                <p>✓ Dependency Vulnerability Scanning - Safety</p>
                <p>✓ Infrastructure as Code Scanning - Checkov</p>
            </div>
        </div>
    """
    
    # Add Bandit results
    if bandit_report:
        issues_count = len(bandit_report.get('results', []))
        html_content += f"""
        <div class="section {'critical' if issues_count > 0 else 'info'}">
            <h2>Static Code Analysis (Bandit)</h2>
            <p>Issues found: {issues_count}</p>
        """
        
        if issues_count > 0:
            html_content += "<ul>"
            for issue in bandit_report.get('results', [])[:5]:  # Show first 5 issues
                html_content += f"<li><strong>{issue.get('test_name', 'Unknown')}</strong>: {issue.get('issue_text', 'No description')}</li>"
            html_content += "</ul>"
        
        html_content += "</div>"
    
    # Add Safety results
    if safety_report:
        vulns = safety_report if isinstance(safety_report, list) else []
        html_content += f"""
        <div class="section {'warning' if len(vulns) > 0 else 'info'}">
            <h2>Dependency Vulnerability Scan (Safety)</h2>
            <p>Vulnerabilities found: {len(vulns)}</p>
        """
        
        if len(vulns) > 0:
            html_content += "<ul>"
            for vuln in vulns[:5]:  # Show first 5 vulnerabilities
                html_content += f"<li><strong>{vuln.get('package', 'Unknown package')}</strong>: {vuln.get('advisory', 'No advisory')}</li>"
            html_content += "</ul>"
        
        html_content += "</div>"
    
    # Add Checkov results
    if checkov_report:
        failed_checks = checkov_report.get('results', {}).get('failed_checks', [])
        html_content += f"""
        <div class="section {'warning' if len(failed_checks) > 0 else 'info'}">
            <h2>Infrastructure Scan (Checkov)</h2>
            <p>Failed checks: {len(failed_checks)}</p>
        """
        
        if len(failed_checks) > 0:
            html_content += "<ul>"
            for check in failed_checks[:5]:  # Show first 5 failed checks
                html_content += f"<li><strong>{check.get('check_id', 'Unknown')}</strong>: {check.get('check_name', 'No description')}</li>"
            html_content += "</ul>"
        
        html_content += "</div>"
    
    html_content += """
        <div class="section info">
            <h2>Recommendations</h2>
            <ul>
                <li>Review and fix all critical and high-severity security issues</li>
                <li>Update dependencies with known vulnerabilities</li>
                <li>Implement security best practices in infrastructure code</li>
                <li>Regular security scanning in CI/CD pipeline</li>
            </ul>
        </div>
    </body>
    </html>
    """
    
    with open('security-summary.html', 'w') as f:
        f.write(html_content)
    
    print("Security report generated: security-summary.html")

if __name__ == "__main__":
    generate_html_report()
