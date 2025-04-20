import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
from typing import Dict, Any
import os

class MLDetector:
    def __init__(self):
        self.model_path = 'fake_account_model.joblib'
        self.scaler_path = 'feature_scaler.joblib'
        self.model = None
        self.scaler = None
        self.load_or_train_model()

    def load_or_train_model(self):
        """Load existing model or train a new one if not available"""
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
        else:
            self.train_model()

    def train_model(self):
        """Train a new model with synthetic data (in a real scenario, this would use labeled data)"""
        # Generate synthetic training data
        n_samples = 1000
        X = np.random.rand(n_samples, 7)  # 7 features
        y = np.random.randint(0, 2, n_samples)  # Binary labels

        # Scale features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_scaled, y)

        # Save model and scaler
        joblib.dump(self.model, self.model_path)
        joblib.dump(self.scaler, self.scaler_path)

    def extract_features(self, account_features: Dict[str, Any]) -> np.ndarray:
        """Extract and prepare features for the ML model"""
        features = [
            account_features['followers_count'],
            account_features['following_count'],
            account_features['tweet_count'],
            account_features['account_age_days'],
            float(account_features['has_profile_image']),
            float(account_features['has_description']),
            account_features.get('engagement_rate', 0)
        ]
        return np.array(features).reshape(1, -1)

    def predict(self, account_features: Dict[str, Any]) -> float:
        """Predict the probability of an account being fake"""
        try:
            features = self.extract_features(account_features)
            features_scaled = self.scaler.transform(features)
            # Get probability of being fake (class 1)
            return self.model.predict_proba(features_scaled)[0][1]
        except Exception as e:
            print(f"Error in ML prediction: {str(e)}")
            return 0.5  # Return neutral score if prediction fails 