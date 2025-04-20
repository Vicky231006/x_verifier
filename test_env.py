import os
from dotenv import load_dotenv
import pathlib

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Print .env file path
env_path = pathlib.Path('.') / '.env'
print(f"\n.env file path: {env_path.absolute()}")
print(f".env file exists: {env_path.exists()}")

# Try to read .env file directly
if env_path.exists():
    print("\nContents of .env file:")
    with open('.env', 'r') as f:
        print(f.read())

# Load environment variables
print("\nTrying to load environment variables...")
load_dotenv(verbose=True)

# Check environment variables
print("\nChecking environment variables:")
vars_to_check = [
    'TWITTER_API_KEY',
    'TWITTER_API_SECRET',
    'TWITTER_ACCESS_TOKEN',
    'TWITTER_ACCESS_TOKEN_SECRET',
    'TWITTER_BEARER_TOKEN'
]

for var in vars_to_check:
    value = os.getenv(var)
    if value:
        print(f"{var}: {value[:5]}...{value[-5:] if len(value) > 10 else ''}")
    else:
        print(f"{var}: Not found!") 