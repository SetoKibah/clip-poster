# config/settings.py

import os

# Fetching Environment Variables

# Twitter API Credentials
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY', 'default_twitter_api_key')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET', 'default_twitter_secret')
# TikTok API Credentials
TIKTOK_API_KEY = os.environ.get('TIKTOK_API_KEY', 'default_tiktok_api_key')
TIKTOK_API_SECRET = os.environ.get('TIKTOK_API_SECRET', 'default_tiktok_api_secret')

# Regular Configuration Variables
CLIP_LENGTH = 60
CLIP_FORMAT = 'mp4'
VIDEO_RESOLUTION = '720p'
MAX_RETRIES = 3
LOG_FILE_PATH = 'logs/app.log'