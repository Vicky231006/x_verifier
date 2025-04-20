import os
from dotenv import load_dotenv
from rule_based_detector import RuleBasedDetector
from ml_detector import MLDetector
import tweepy
import pandas as pd
from typing import Dict, Any
from datetime import datetime, timezone
import math

class FakeAccountDetector:
    def __init__(self):
        load_dotenv()
        self.rule_detector = RuleBasedDetector()
        self.ml_detector = MLDetector()
        
        # Initialize Twitter API client
        self.client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
            wait_on_rate_limit=False  # We'll handle rate limits ourselves
        )

    def analyze_twitter_account(self, username: str) -> Dict[str, Any]:
        """
        Analyze a Twitter account for potential fake indicators
        """
        try:
            # Get user information
            user = self.client.get_user(username=username, user_fields=[
                'created_at', 'public_metrics', 'verified', 'profile_image_url', 'description'
            ])

            if not user.data:
                return {
                    'error': f'User @{username} not found',
                    'status_code': 404
                }

            user_data = user.data

            # Calculate account age in days
            created_at = user_data.created_at
            account_age_days = (datetime.now(timezone.utc) - created_at).days

            # Get metrics
            metrics = user_data.public_metrics
            followers_count = metrics['followers_count']
            following_count = metrics['following_count']
            tweets_count = metrics['tweet_count']

            # Calculate risk factors
            risk_factors = []
            total_risk = 0

            # 1. Account age (newer accounts are riskier)
            age_risk = max(0, 1 - (account_age_days / 365))  # Accounts less than a year old are risky
            risk_factors.append(('account_age', age_risk))

            # 2. Followers to following ratio
            if following_count > 0:
                ratio = followers_count / following_count
                ratio_risk = 1 - min(1, ratio / 2)  # Ratio less than 0.5 is suspicious
                risk_factors.append(('follower_ratio', ratio_risk))

            # 3. Profile completeness
            profile_risk = 0
            if not user_data.profile_image_url:
                profile_risk += 0.5
            if not user_data.description:
                profile_risk += 0.5
            risk_factors.append(('profile_completeness', profile_risk))

            # 4. Tweet activity
            tweet_risk = max(0, 1 - (tweets_count / 100))  # Less than 100 tweets is suspicious
            risk_factors.append(('tweet_activity', tweet_risk))

            # Calculate overall risk (average of all factors)
            total_risk = sum(risk[1] for risk in risk_factors) / len(risk_factors)
            risk_percentage = math.floor(total_risk * 100)

            return {
                'risk_percentage': risk_percentage,
                'followers_count': followers_count,
                'following_count': following_count,
                'tweets_count': tweets_count,
                'account_age_days': account_age_days,
                'is_verified': user_data.verified,
                'has_profile_image': bool(user_data.profile_image_url),
                'has_description': bool(user_data.description)
            }

        except tweepy.TooManyRequests as e:
            # Get the wait time from the response headers
            try:
                wait_time = int(e.response.headers.get('x-rate-limit-reset', 0)) - int(datetime.now().timestamp())
                wait_time = max(1, wait_time)  # Ensure wait time is at least 1 second
            except (ValueError, AttributeError):
                wait_time = 60  # Default to 60 seconds if we can't get the actual wait time

            return {
                'error': 'Rate limit exceeded. Please try again later.',
                'status_code': 429,
                'wait_time': wait_time
            }

        except tweepy.HTTPException as e:
            return {
                'error': str(e),
                'status_code': e.response.status_code if hasattr(e, 'response') else 500
            }

        except Exception as e:
            return {
                'error': str(e),
                'status_code': 500
            }

if __name__ == "__main__":
    detector = FakeAccountDetector()
    result = detector.analyze_twitter_account("example_username")
    print(result)