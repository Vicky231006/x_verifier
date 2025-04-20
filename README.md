# X Verifier - Twitter Account Authenticity Checker

A powerful tool to analyze Twitter/X accounts and determine their authenticity using various metrics and machine learning techniques.

## 🌟 Features

- Real-time account analysis
- Multiple authenticity indicators:
  - Account age evaluation
  - Follower-following ratio analysis
  - Profile completeness check
  - Tweet activity assessment
- Visual trust indicators
- Rate limit handling with countdown timer
- Verified account badge display
- Beautiful, responsive UI

## 🚀 Live Demo

[Coming soon]

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Vicky231006/x_verifier.git
cd x_verifier
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory with your Twitter API credentials:
```env
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

## 🚀 Running the Application

1. Make sure your virtual environment is activated

2. Start the Flask server:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## 🔧 Configuration

The application uses the following environment variables:
- `TWITTER_API_KEY`: Your Twitter API key
- `TWITTER_API_SECRET`: Your Twitter API secret
- `TWITTER_ACCESS_TOKEN`: Your Twitter access token
- `TWITTER_ACCESS_TOKEN_SECRET`: Your Twitter access token secret
- `TWITTER_BEARER_TOKEN`: Your Twitter bearer token

To obtain these credentials:
1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new project and app
3. Generate the required tokens and keys
4. Add them to your `.env` file

## 📁 Project Structure

```
x_verifier/
├── app.py                 # Main Flask application
├── fake_account_detector.py   # Core detection logic
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── templates/
│   └── index.html        # Frontend template
└── README.md             # Documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Contact

Your Name - [@Vicky231006](https://github.com/Vicky231006)

Project Link: [https://github.com/Vicky231006/x_verifier](https://github.com/Vicky231006/x_verifier) 