#!/usr/bin/env python3

import hvac
import os
import sys

def get_secrets_from_vault():
    """Retrieve secrets from Vault"""
    
    # Initialize Vault client
    client = hvac.Client(url='http://localhost:8200')
    
    # Authenticate (in production, use proper auth methods)
    vault_token = os.getenv('VAULT_TOKEN')
    if not vault_token:
        print("Error: VAULT_TOKEN environment variable not set")
        sys.exit(1)
    
    client.token = vault_token
    
    try:
        # Read secrets
        secret_response = client.secrets.kv.v2.read_secret_version(
            path='app/config'
        )
        
        secrets = secret_response['data']['data']
        
        print("Successfully retrieved secrets from Vault:")
        for key in secrets.keys():
            print(f"- {key}: {'*' * len(secrets[key])}")
        
        return secrets
        
    except Exception as e:
        print(f"Error retrieving secrets: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_secrets_from_vault()
