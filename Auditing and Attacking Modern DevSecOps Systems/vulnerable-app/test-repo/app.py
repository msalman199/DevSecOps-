import os

# Bad practice - hardcoded secrets
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_URL = "postgresql://user:password123@localhost:5432/mydb"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_to_database():
    password = "super_secret_password"
    return f"Connecting with {password}"
