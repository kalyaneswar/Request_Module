import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch GitHub OAuth app credentials from environment
CLIENT_ID = os.getenv('API_KEY')          # GitHub OAuth Client ID
CLIENT_SECRET = os.getenv('SECRET_KEY')   # GitHub OAuth Client Secret

# GitHub endpoints
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
BASE_URL = 'https://api.github.com'

# Initialize Flask app
app = Flask(__name__)

# Route to display login link
@app.route('/')
def index():
    # Redirect user to GitHub OAuth authorization page
    return f'<a href="https://github.com/login/oauth/authorize?client_id={CLIENT_ID}">Login with GitHub</a>'

# GitHub callback route after user authorizes
@app.route('/authorize')
def authorize():
    # Get the authorization code returned by GitHub
    code = request.args.get('code')
    if not code:
        return "Missing code", 400

    # Prepare data for token exchange
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    # Request access token from GitHub
    headers = {'Accept': 'application/json'}
    r = requests.post(GITHUB_TOKEN_URL, data=data, headers=headers)
    token = r.json().get('access_token')

    # Check if token was successfully retrieved
    if not token:
        return "Authorization failed", 401

    # Use the token to access the user's repositories
    headers['Authorization'] = f'token {token}'
    r2 = requests.get(BASE_URL + '/user/repos', headers=headers)

    repos = r2.json()
    # Validate response is a list of repositories
    if not isinstance(repos, list):
        return "Failed to fetch repositories", 400

    # Extract repository names
    repo_names = [repo['name'] for repo in repos]

    # Display repository names in browser (line break separated)
    return '<br>'.join(repo_names)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
