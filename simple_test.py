import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
print(f"Bearer token starts with: {bearer_token[:15]}...")

try:
    print("\nInitializing Twitter client...")
    client = tweepy.Client(bearer_token=bearer_token)
    
    print("\nTrying to fetch a specific user...")
    # Try to get Twitter's own account info (a very basic request)
    user = client.get_user(username="Twitter")
    
    if user.data:
        print("\nSuccess! User data retrieved:")
        print(f"Username: {user.data.username}")
        print(f"ID: {user.data.id}")
    else:
        print("No user data found")

except tweepy.TweepyException as e:
    print(f"\nTwitter API Error: {str(e)}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Status code: {e.response.status_code}")
        print(f"Response text: {e.response.text}")
    
except Exception as e:
    print(f"\nGeneral Error: {str(e)}")

print("\nScript execution completed") 