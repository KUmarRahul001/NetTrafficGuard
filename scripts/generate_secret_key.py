# scripts/generate_secret_key.py

import os
import binascii

def generate_secret_key():
    """Generate a random secret key."""
    secret_key = binascii.hexlify(os.urandom(24)).decode()
    return secret_key

def save_secret_key_to_env(secret_key, file_path='file.env'):
    """Save the generated secret key to the .env file."""
    with open(file_path, 'w') as file:
        file.write(f'SECRET_KEY={secret_key}\n')

if __name__ == '__main__':
    key = generate_secret_key()
    save_secret_key_to_env(key)
    print(f'Secret key generated and saved to file.env: {key}')
