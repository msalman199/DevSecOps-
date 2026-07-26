import os
import requests

# Bad practice - hardcoded secrets
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "super_secret_password123"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_to_database():
    connection_string = f"postgresql://user:{DATABASE_PASSWORD}@localhost:5432/mydb"
    return connection_string

def call_api():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

if __name__ == "__main__":
    print("Application started")
