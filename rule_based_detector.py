from typing import Dict, Any

class RuleBasedDetector:
    def __init__(self):
        # Define thresholds for various rules
        self.thresholds = {
            'min_followers': 10,
            'max_following_ratio': 10,  # Following/Followers ratio
            'min_account_age_days': 7,
            'max_tweets_per_day': 50,
            'min_engagement_rate': 0.01  # Likes per tweet
        }

    def analyze(self, features: Dict[str, Any]) -> float:
        """
        Analyze account features using rule-based heuristics
        Returns a score between 0 and 1, where 1 indicates highest likelihood of being fake
        """
        risk_score = 0.0
        total_rules = 0

        # Rule 1: Check follower count
        if features['followers_count'] < self.thresholds['min_followers']:
            risk_score += 0.2
        total_rules += 1

        # Rule 2: Check following/followers ratio
        if features['following_count'] > 0:
            ratio = features['following_count'] / max(features['followers_count'], 1)
            if ratio > self.thresholds['max_following_ratio']:
                risk_score += 0.15
        total_rules += 1

        # Rule 3: Check account age
        if features['account_age_days'] < self.thresholds['min_account_age_days']:
            risk_score += 0.15
        total_rules += 1

        # Rule 4: Check tweet frequency
        if 'avg_tweets_per_day' in features:
            if features['avg_tweets_per_day'] > self.thresholds['max_tweets_per_day']:
                risk_score += 0.15
        total_rules += 1

        # Rule 5: Check engagement rate
        if 'engagement_rate' in features:
            if features['engagement_rate'] < self.thresholds['min_engagement_rate']:
                risk_score += 0.15
        total_rules += 1

        # Rule 6: Check profile completeness
        if not features['has_profile_image']:
            risk_score += 0.1
        if not features['has_description']:
            risk_score += 0.1
        total_rules += 2

        # Normalize the score
        return risk_score / total_rules 