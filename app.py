from flask import Flask, render_template, request, jsonify
from fake_account_detector import FakeAccountDetector
import os
from dotenv import load_dotenv
import tweepy

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Verify Twitter credentials are loaded
required_env_vars = [
    'TWITTER_API_KEY',
    'TWITTER_API_SECRET',
    'TWITTER_ACCESS_TOKEN',
    'TWITTER_ACCESS_TOKEN_SECRET',
    'TWITTER_BEARER_TOKEN'
]

missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")

detector = FakeAccountDetector()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        username = request.form.get('username')
        if not username:
            return jsonify({'error': 'Username is required'}), 400
        
        # Remove @ symbol if present
        username = username.lstrip('@')
        
        # Analyze the account
        result = detector.analyze_twitter_account(username)
        
        if isinstance(result, dict) and 'error' in result:
            error_msg = result['error']
            status_code = result.get('status_code', 400)
            
            # If it's a rate limit error, include the wait time
            if 'rate limit' in error_msg.lower():
                return jsonify({
                    'error': error_msg,
                    'wait_time': result.get('wait_time', 60)  # Default to 60 seconds if not specified
                }), status_code
            
            return jsonify({'error': error_msg}), status_code
        
        # Calculate genuinity percentage (inverse of risk percentage)
        genuinity = 100 - result.get('risk_percentage', 0)
        
        return jsonify({
            'username': username,
            'genuinity': genuinity,
            'details': {
                'followers': result.get('followers_count', 0),
                'following': result.get('following_count', 0),
                'tweets': result.get('tweets_count', 0),
                'account_age': result.get('account_age_days', 0),
                'verified': 'Yes' if result.get('is_verified', False) else 'No',
                'has_profile_image': 'Yes' if result.get('has_profile_image', False) else 'No',
                'has_description': 'Yes' if result.get('has_description', False) else 'No'
            }
        })
    except tweepy.TooManyRequests as e:
        return jsonify({
            'error': 'Rate limit exceeded. Please try again later.',
            'wait_time': 60  # Default wait time for rate limits
        }), 429
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 