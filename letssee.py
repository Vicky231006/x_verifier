import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Print environment variables (with partial hiding for security)
print("Checking environment variables:")
for var in ['TWITTER_API_KEY', 'TWITTER_API_SECRET', 'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET', 'TWITTER_BEARER_TOKEN']:
    value = os.getenv(var)
    if value:
        print(f"{var}: {value[:5]}...{value[-5:] if len(value) > 10 else ''}")
    else:
        print(f"{var}: Not found!")

try:
    print("\nInitializing Twitter client...")
    client = tweepy.Client(
        bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
        consumer_key=os.getenv('TWITTER_API_KEY'),
        consumer_secret=os.getenv('TWITTER_API_SECRET'),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    
    print("Client initialized successfully!")
    
    print("\nTrying to fetch user data...")
    user = client.get_user(username="elonmusk")
    
    if user.data:
        print("\nUser data retrieved successfully:")
        print(f"ID: {user.data.id}")
        print(f"Name: {user.data.name}")
        print(f"Username: {user.data.username}")
    else:
        print("No user data returned")

except tweepy.TweepyException as e:
    print(f"\nTwitter API Error: {str(e)}")
except Exception as e:
    print(f"\nGeneral Error: {str(e)}")

print("\nScript execution completed")