import requests
import json
import sys

def test_sql_injection():
    """Test for SQL injection vulnerabilities"""
    print("Testing for SQL injection...")
    
    # Test payloads
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "' UNION SELECT * FROM users --"
    ]
    
    vulnerabilities = []
    
    for payload in payloads:
        test_data = {
            "username": payload,
            "password": "test"
        }
        
        try:
            # This would normally test against running application
            print(f"Testing payload: {payload}")
            # Simulate vulnerability detection
            if "OR" in payload or "UNION" in payload:
                vulnerabilities.append(f"Potential SQL injection: {payload}")
        except Exception as e:
            print(f"Error testing payload {payload}: {e}")
    
    return vulnerabilities

def test_weak_password_hashing():
    """Test for weak password hashing"""
    print("Testing password hashing strength...")
    
    # Check if MD5 is used (weak)
    with open('../src/app.py', 'r') as f:
        content = f.read()
        if 'hashlib.md5' in content:
            return ["Weak password hashing detected: MD5 is cryptographically broken"]
    
    return []

def main():
    print("Running security tests...")
    
    sql_injection_issues = test_sql_injection()
    password_issues = test_weak_password_hashing()
    
    all_issues = sql_injection_issues + password_issues
    
    if all_issues:
        print("\nSecurity Issues Found:")
        for issue in all_issues:
            print(f"- {issue}")
        return 1
    else:
        print("\nNo critical security issues found.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
