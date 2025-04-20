import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    print("Testing with Bearer Token only...")
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'))
    
    print("\nTrying to fetch Twitter public data...")
    # Try a simple search query
    tweets = client.search_recent_tweets(query="twitter", max_results=10)
    
    if tweets.data:
        print("\nSuccess! Retrieved some tweets:")
        for tweet in tweets.data[:3]:
            print(f"Tweet ID: {tweet.id}")
    else:
        print("No tweets found, but API call was successful")

except tweepy.TweepyException as e:
    print(f"\nTwitter API Error: {str(e)}")
    print("\nError Details:")
    print(f"Error Code: {getattr(e, 'code', 'N/A')}")
    print(f"Error Message: {getattr(e, 'response', {}).get('message', 'No message')}")
    
except Exception as e:
    print(f"\nGeneral Error: {str(e)}")

print("\nScript execution completed") 